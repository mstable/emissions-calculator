import numpy as np
from datetime import datetime, timedelta
import requests
from enum import Enum
from helper import iso_date_to_datetime, datetime_to_timestamp
from config import *


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
}""" % (
        unix_ts
    )

    try:
        response = requests.post(
            "https://api.thegraph.com/subgraphs/name/blocklytics/ethereum-blocks",
            json={"query": query},
        )
        blknum = int(response.json()["data"]["blocks"][0]["number"])
    except:
        raise Exception(
            "There was a problem for getting the block number for timestamp %d"
            % (unix_ts)
        )

    return blknum


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
}""" % (
        schema,
        start_ts,
        schema,
        end_ts,
    )

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
  }""" % (
            number,
            schema,
            number,
        )

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

    response = requests.post(url, json={"query": query})

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

    response = requests.post(url, json={"query": query})
    data = response.json()["data"]

    points = list(data.values())
    liq_array_dict = {}

    for point in points:
        for token_dict in point:
            symbol = token_dict["token"]["symbol"]
            if symbol not in liq_array_dict:
                liq_array_dict[symbol] = []

            liq_array_dict[symbol].append(float(token_dict["totalSupply"]["simple"]))

    result = {}
    for symbol, liq_array in liq_array_dict.items():
        result[symbol] = np.mean(liq_array)

    return result


def get_btc_price_url(datetime):
    date_str = datetime.strftime("%d-%m-%Y")
    return "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=%s" % (date_str)


def get_btc_price(datetime):
    url = get_btc_price_url(datetime)
    response = requests.get(url)

    if not response.ok:
        raise Exception(
            "There was a problem while fetching the BTC price: %s" % (response.text)
        )

    data = response.json()
    price = data["market_data"]["current_price"]["usd"]

    if not 100 <= price <= 10_000_000:
        raise Exception("Coingecko returned an unusual price.")

    return price
