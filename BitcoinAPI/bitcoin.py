from pycoingecko import *


def getBitcoinCurrentPrice(curr='inr'):
    bitcoin = CoinGeckoAPI()
    current_price = bitcoin.get_price(ids='bitcoin', vs_currencies=curr)
    return current_price


def getBitcoinListUsingTimestamp(currency, from_timestamp, to_timestamp):
    bitcoin = CoinGeckoAPI()
    bitcoin_list = bitcoin.get_coin_market_chart_range_by_id(
        id='bitcoin', vs_currency=currency, from_timestamp=from_timestamp, to_timestamp=to_timestamp)
    return bitcoin_list
