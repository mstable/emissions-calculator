import argparse
import requests

from scrape import *
from top_level_schedule import TOP_LEVEL_SCHEDULE, get_most_recent_date


example_text = """Example:
python compute_emissions.py 2021-04-01 100_000"""

# Argument parser config
parser = argparse.ArgumentParser(
    epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument(
    "-d", "--date",
    type=str,
    help="The emissions will be computed for the week preceding this date.",
)
parser.add_argument(
    "--offset",
    type=int,
    default=86400,
    help="Offset (to the past) in seconds which data will be scraped. Default: 86400 (1 day)",
)
# parser.add_argument(
#     "total_emission", type=float,
#     help="Total emission for the interval.")


def __main__():
    args = parser.parse_args()

    if not 0 <= args.offset <= 7 * 86400:
        raise ValueError("Offset must be between 0 and 7 days.")

    if args.date:
        date = args.date
    else:
        now =  datetime.utcnow()
        date = get_most_recent_date(now, args.offset)

        if not date:
            raise ValueError("No entry found for %s in the top level emission schedule"%(now))

    end_dt = iso_date_to_datetime(date)
    start_dt = end_dt - timedelta(days=7)

    if not start_dt.weekday() == end_dt.weekday() == 0:
        raise ValueError("Input dates are restricted to Mondays.")


    # Get timestamps
    start_ts = datetime_to_timestamp(start_dt)
    end_ts = datetime_to_timestamp(end_dt)

    # Get block numbers
    start_blk = get_block_number(start_ts - args.offset)
    end_blk = get_block_number(end_ts - args.offset)

    price_check_dt = end_dt - timedelta(seconds=args.offset)

    print("Getting BTC price for %s" % (price_check_dt))
    btc_price = get_btc_price(price_check_dt)

    print("Scraping mAsset volumes")
    masset_volumes = get_vol(start_blk, end_blk, Mode.MASSET)

    print("Scraping feeder pool volumes")
    fp_volumes = get_vol(start_blk, end_blk, Mode.FEEDER_POOL)

    print("Scraping mAsset liquidities")
    masset_liquidities = get_liq(start_blk, end_blk, Mode.MASSET)

    print("Scraping feeder pool liquidities")
    fp_liquidities = get_liq(start_blk, end_blk, Mode.FEEDER_POOL)

    masset_symbols = symbols = list(
        set(list(masset_volumes.keys())).union(set(list(masset_liquidities.keys())))
    )

    fp_symbols = list(
        set(list(fp_volumes.keys())).union(set(list(fp_liquidities.keys())))
    )

    deprecated = TOP_LEVEL_SCHEDULE[date]['skip']
    fp_symbols = list(filter(lambda x: x not in deprecated, fp_symbols))

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

    ###############################
    # Using the logic from MCCP-4 #
    ###############################

    top_level_dict = TOP_LEVEL_SCHEDULE[date]
    top_level_dict.pop("skip")
    pools_emission = top_level_dict["pools"]
    total_emission = sum(top_level_dict.values())

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


    vault_emission = pools_emission * (1 - FEEDER_EMISSION_PCT)
    feeder_emission = pools_emission * FEEDER_EMISSION_PCT

    feeder_base_emission = feeder_emission * BASE_FEEDER_EMISSION_PCT / n
    vault_base_emission = vault_emission * BASE_VAULT_EMISSION_PCT / m

    # Compute bonus coefficients
    bonus_feeder_factor = []
    bonus_vault_factor = []

    for supply, volume in zip(feeder_supplies, feeder_volumes):
        bonus_feeder_factor.append(volume / supply ** (1 / 4))

    for supply, volume in zip(masset_supplies, masset_volumes):
        bonus_vault_factor.append(volume / supply ** (1 / 4))

    print()
    print("Here are the weekly emissions to be paid out on %s" % (date))
    print("On-chain data has been scraped with %g day offset" % (args.offset / 86400))

    print()
    print("Total emission: %.2f MTA" % (total_emission))
    print("Emission to native pools: %.2f MTA" % (pools_emission))

    print()

    print("BTC price: %.2f USD" % (btc_price))

    print("Base emission to vaults: %.2f MTA each" % vault_base_emission)
    print("Base emission to feeder pools: %.2f MTA each" % feeder_base_emission)
    print()
    print("Ethereum pools")

    if "staking-v2-mta" in top_level_dict:
        print("Staking-v2-MTA - Emission: %.2f MTA" % (top_level_dict["staking-v2-mta"]))

    if "staking-v2-bpt" in top_level_dict:
        print("Staking-v2-BPT - Emission: %.2f MTA" % (top_level_dict["staking-v2-bpt"]))

    if "MTA/WETH" in top_level_dict:
        print("MTA/WETH pool - Emission: %.2f MTA" % (top_level_dict["MTA/WETH"]))

    vault_emissions = []
    for i in range(m):
        bonus_emission = (
            vault_emission
            * (1 - BASE_VAULT_EMISSION_PCT)
            * bonus_vault_factor[i]
            / sum(bonus_vault_factor)
        )
        
        total_vault_emission = vault_base_emission + bonus_emission
        vault_emissions.append(total_vault_emission)

        lur = masset_volumes[i] / masset_supplies[i]

        print(
            "%s vault - Liq: %.2fm USD - Vol: %.2fm USD - LUR: %.2f%% - Emission: %.2f MTA"
            % (
                masset_symbols[i],
                masset_supplies[i] / 1e6,
                masset_volumes[i] / 1e6,
                lur * 100,
                total_vault_emission,
            )
        )

    feeder_emissions = []
    for i in range(n):
        bonus_emission = (
            feeder_emission
            * (1 - BASE_FEEDER_EMISSION_PCT)
            * bonus_feeder_factor[i]
            / sum(bonus_feeder_factor)
        )

        total_feeder_emission = feeder_base_emission + bonus_emission
            
        feeder_emissions.append(total_feeder_emission)
        lur = feeder_volumes[i] / feeder_supplies[i]

        print(
            "Feeder %s - Liq: %.2fm USD - Vol: %.2fm USD - LUR: %.2f%% - Emission: %.2f MTA"
            % (
                fp_symbols[i],
                feeder_supplies[i] / 1e6,
                feeder_volumes[i] / 1e6,
                lur * 100,
                total_feeder_emission,
            )
        )

    print(
        "Feeder fPmUSD/RAI - Emission: %.2f MTA"
        % (
            top_level_dict["fPmUSD/RAI"]
        )
    )

    assert abs(vault_emission + sum(feeder_emissions) - pools_emission) <= 1e-5

    print()
    print("Polygon")

    if "p-imUSD" in top_level_dict:
        print("imUSD vault - Emission: %.2f MTA" % (top_level_dict["p-imUSD"]))

    if "p-MTA" in top_level_dict:
        print("MTA balancer pool - Emission: %.2f MTA" % (top_level_dict["p-MTA"]))

    if "p-frax" in top_level_dict:
        print("fpFrax - Emission: %.2f MTA" % (top_level_dict["p-frax"]))


if __name__ == "__main__":
    __main__()
