import requests

def get_btc_price_url(datetime):
    date_str = datetime.strftime("%d-%m-%Y")
    return "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=%s"%(date_str)

def get_btc_price(datetime):
    url = get_btc_price_url(datetime)
    response = requests.get(url)

    if not response.ok:
        raise Exception("There was a problem while fetching the BTC price: %s"%(response.text))

    data = response.json()
    price = data["market_data"]["current_price"]["usd"]

    if not 100 <= price <= 10_000_000:
        raise Exception("Coingecko returned an unusual price.")

    return price

