import argparse
import requests
import numpy as np
from datetime import datetime, timedelta
from enum import Enum

from prices import get_btc_price

# Percentage of mAsset emission that goes to feeders
FEEDER_EMISSION_PCT = 0.80

WEIGHTED_AVERAGE_SAMPLES = 500

# Base emission that gets equally distributed to feeders
BASE_FEEDER_EMISSION_PCT = 0.20
BASE_VAULT_EMISSION_PCT = 0.50

# Subgraph URLs
PROTOCOL_URL = "https://api.thegraph.com/subgraphs/name/mstable/mstable-protocol"
FEEDER_POOL_URL = "https://api.thegraph.com/subgraphs/name/mstable/mstable-feeder-pools"

example_text = """Example:
python compute_emissions.py 2021-04-01 100_000"""

# Argument parser config
parser = argparse.ArgumentParser(
    epilog=example_text,
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument(
    "date", type=str,
    help="The emissions will be computed for the week preceding this date.")
# parser.add_argument(
#     "btc_price", type=float,
#     help="BTC price at the end of the interval.")
parser.add_argument(
    "total_emission", type=float,
    help="Total emission for the interval.")


class Mode(Enum):
    MASSET = 0
    FEEDER_POOL = 1


def get_block_number(unix_ts):
    "Get the block number corresponding to a UNIX timestamp"
    query = """
{
  blocks(first: 1, orderBy: timestamp, orderDirection: asc, where: {timestamp_gt: "%d"}) {
    id
    number
    timestamp
  }
}"""%(unix_ts)

    response = requests.post("https://api.thegraph.com/subgraphs/name/blocklytics/ethereum-blocks", json={'query': query})
    blknum = int(response.json()["data"]["blocks"][0]["number"])
    return blknum

def iso_date_to_datetime(date_str):
    "Convert ISO date to Python datetime object"
    dt = datetime.strptime(date_str, '%Y-%m-%d')
    return dt

def datetime_to_timestamp(dt):
    "Convert datetime to UNIX timestamp"
    timestamp = int((dt - datetime(1970, 1, 1)).total_seconds())
    return timestamp

def get_vol_query(start_ts, end_ts, mode):
    "Get the query for scraping volumes from the subgraph"

    if mode == Mode.MASSET:
        schema = "massets"
    elif mode == Mode.FEEDER_POOL:
        schema = "feederPools"
    else:
        raise ValueError

    result = """
{
  start: %s(block: { number:%d }) {
    id
    token	{
      symbol
    }
    cumulativeMinted {
      simple
    }
    cumulativeSwapped {
      simple
    }
    cumulativeRedeemed {
      simple
    }
  }
  end: %s(block: { number:%d }) {
    id
    token	{
      symbol
    }
    cumulativeMinted {
      simple
    }
    cumulativeSwapped {
      simple
    }
    cumulativeRedeemed {
      simple
    }
  }
}"""%(schema, start_ts, schema, end_ts)

    return result


def get_liq_query(start_blk, end_blk, mode):
    "Get the query for scraping liquidities from the subgraph"
    if mode == Mode.MASSET:
        schema = "massets"
    elif mode == Mode.FEEDER_POOL:
        schema = "feederPools"
    else:
        raise ValueError

    numbers = np.linspace(
        start_blk,
        end_blk,
        min(WEIGHTED_AVERAGE_SAMPLES, end_blk - start_blk),
        dtype=int,
    )

    query = "{\n"

    for number in numbers:
        query += """
  t%d: %s(block:{number: %d}) {
    id
    token {
      symbol
    }
    totalSupply {
      simple
    }
  }"""%(number, schema, number)

    query += "\n}"
    return query

def get_vol(start_blk, end_blk, mode):
    query = get_vol_query(start_blk, end_blk, mode)

    if mode == Mode.MASSET:
        url = PROTOCOL_URL
    elif mode == Mode.FEEDER_POOL:
        url = FEEDER_POOL_URL
    else:
        raise ValueError

    response = requests.post(
        url,
        json={'query': query}
    )

    data = response.json()["data"]

    start_data = data["start"]
    end_data = data["end"]

    initial_vol = {}
    final_vol = {}

    for i in start_data:
        symbol = i["token"]["symbol"]
        initial_vol[symbol] = 0
        initial_vol[symbol] += float(i["cumulativeMinted"]["simple"]) / 2
        initial_vol[symbol] += float(i["cumulativeRedeemed"]["simple"]) / 2
        initial_vol[symbol] += float(i["cumulativeSwapped"]["simple"])

    for i in end_data:
        symbol = i["token"]["symbol"]
        final_vol[symbol] = 0
        final_vol[symbol] += float(i["cumulativeMinted"]["simple"]) / 2
        final_vol[symbol] += float(i["cumulativeRedeemed"]["simple"]) / 2
        final_vol[symbol] += float(i["cumulativeSwapped"]["simple"])

    symbols = list(set(list(initial_vol.keys())).union(set(list(final_vol.keys()))))
    volumes = {}
    for symbol in symbols:
        if symbol in initial_vol and symbol in final_vol:
            volumes[symbol] = final_vol[symbol] - initial_vol[symbol]
        elif symbol not in initial_vol and symbol in final_vol:
            volumes[symbol] = final_vol[symbol]
        else:
            volumes[symbol] = 0

    return volumes


def get_liq(start_blk, end_blk, mode):
    query = get_liq_query(start_blk, end_blk, mode)

    if mode == Mode.MASSET:
        url = PROTOCOL_URL
    elif mode == Mode.FEEDER_POOL:
        url = FEEDER_POOL_URL
    else:
        raise ValueError

    response = requests.post(
        url,
        json={'query': query}
    )
    data = response.json()["data"]

    points = list(data.values())
    liq_array_dict = {}

    for point in points:
        for token_dict in point:
            symbol = token_dict["token"]["symbol"]
            if symbol not in liq_array_dict:
                liq_array_dict[symbol] = []

            liq_array_dict[symbol].append(
                float(token_dict["totalSupply"]["simple"])
            )

    result = {}
    for symbol, liq_array in liq_array_dict.items():
        result[symbol] = np.mean(liq_array)

    return result

def __main__():
    args = parser.parse_args()


    end_dt = iso_date_to_datetime(args.date)
    start_dt = end_dt - timedelta(days=7)

    if not start_dt.weekday() == end_dt.weekday() == 0:
        raise ValueError("Input dates are restricted to Mondays.")

    # Get timestamps
    start_ts = datetime_to_timestamp(start_dt)
    end_ts = datetime_to_timestamp(end_dt)

    # Get block numbers
    start_blk = get_block_number(start_ts)
    end_blk = get_block_number(end_ts)

    print("Getting BTC price for %s"%(end_dt))
    btc_price = get_btc_price(end_dt)

    print("Scraping mAsset volumes")
    masset_volumes = get_vol(start_blk, end_blk, Mode.MASSET)

    print("Scraping feeder pool volumes")
    fp_volumes = get_vol(start_blk, end_blk, Mode.FEEDER_POOL)

    print("Scraping mAsset liquidities")
    masset_liquidities = get_liq(start_blk, end_blk, Mode.MASSET)

    print("Scraping feeder pool liquidities")
    fp_liquidities = get_liq(start_blk, end_blk, Mode.FEEDER_POOL)

    masset_symbols = symbols = list(
        set(list(masset_volumes.keys())).union(set(list(masset_liquidities.keys()))))

    fp_symbols = list(
        set(list(fp_volumes.keys())).union(set(list(fp_liquidities.keys()))))

    masset_vol_arr = [masset_volumes[s] for s in masset_symbols]
    fp_vol_arr = [fp_volumes[s] for s in fp_symbols]

    masset_liq_arr = [masset_liquidities[s] for s in masset_symbols]
    fp_liq_arr = [fp_liquidities[s] for s in fp_symbols]

    for i in range(len(masset_symbols)):
        symbol = masset_symbols[i]
        if "BTC" in symbol:
            masset_vol_arr[i] *= btc_price
            masset_liq_arr[i] *= btc_price

    for i in range(len(fp_symbols)):
        symbol = fp_symbols[i]
        if "BTC" in symbol:
            fp_vol_arr[i] *= btc_price
            fp_liq_arr[i] *= btc_price

    ############################################
    # Using the logic from simple_heuristic.py #
    ############################################

    total_emission = args.total_emission

    # Current pool sizes
    feeder_supplies = fp_liq_arr
    masset_supplies = masset_liq_arr

    # Current weekly volume
    feeder_volumes = fp_vol_arr
    masset_volumes = masset_vol_arr

    #####################
    # Compute emissions #
    #####################

    assert len(feeder_supplies) == len(feeder_volumes)
    m = len(masset_supplies)
    n = len(feeder_supplies)

    if m == 0 or n == 0:
        raise Exception("There needs to be at least 1 feeder pool and 1 mAsset.")

    vault_emission = total_emission * (1 - FEEDER_EMISSION_PCT)
    feeder_emission = total_emission * FEEDER_EMISSION_PCT

    feeder_base_emission = feeder_emission * BASE_FEEDER_EMISSION_PCT / n
    vault_base_emission = vault_emission * BASE_VAULT_EMISSION_PCT / m

    # Compute bonus coefficients
    bonus_feeder_factor = []
    bonus_vault_factor = []

    for supply, volume in zip(feeder_supplies, feeder_volumes):
        bonus_feeder_factor.append(volume / supply**(1/4))

    for supply, volume in zip(masset_supplies, masset_volumes):
        bonus_vault_factor.append(volume / supply**(1/4))

    print("Base emission to vaults: %.2f MTA each"%vault_base_emission)
    print("Base emission to feeder pools: %.2f MTA each"%feeder_base_emission)

    vault_emissions = []
    for i in range(m):
        bonus_emission = vault_emission * (1 - BASE_VAULT_EMISSION_PCT) \
            * bonus_vault_factor[i] / sum(bonus_vault_factor)
        total_vault_emission = vault_base_emission + bonus_emission
        vault_emissions.append(total_vault_emission)

        lur = masset_volumes[i] / masset_supplies[i]

        print("%s vault - Liq: %.2fm USD - Vol: %.2fm USD - LUR: %.2f%% - Emission: %.2f MTA"%(
            masset_symbols[i],
            masset_supplies[i] / 1e6,
            masset_volumes[i] / 1e6,
            lur * 100,
            total_vault_emission,
        ))

    feeder_emissions = []
    for i in range(n):
        bonus_emission = feeder_emission * (1 - BASE_FEEDER_EMISSION_PCT) \
            * bonus_feeder_factor[i] / sum(bonus_feeder_factor)
        total_feeder_emission = feeder_base_emission + bonus_emission
        feeder_emissions.append(total_feeder_emission)

        lur = feeder_volumes[i] / feeder_supplies[i]

        print("Feeder %s - Liq: %.2fm USD - Vol: %.2fm USD - LUR: %.2f%% - Emission: %.2f MTA"%(
            fp_symbols[i],
            feeder_supplies[i] / 1e6,
            feeder_volumes[i] / 1e6,
            lur * 100,
            total_feeder_emission,
        ))

    assert abs(vault_emission + sum(feeder_emissions) - total_emission) <= 1e-5

if __name__ == "__main__":
    __main__()
