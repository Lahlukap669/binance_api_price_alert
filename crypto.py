import os
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
import gmail

api_key = '' #API KEY BINANCE
api_secret = '' #API SECRET

client = Client(api_key, api_secret)
prices = client.get_all_tickers()

depth = client.get_order_book(symbol='SHIBEUR')
shiba = depth['bids'][0][0]

depth = client.get_order_book(symbol='DOGEEUR')
doge = depth['bids'][0][0]

depth = client.get_order_book(symbol='ETHEUR')
eth = depth['bids'][0][0]

depth = client.get_order_book(symbol='BTTEUR')
btt = depth['bids'][0][0]

depth = client.get_order_book(symbol='VETEUR')
vet = depth['bids'][0][0]

depth = client.get_order_book(symbol='MATICEUR')
matic = depth['bids'][0][0]



print("SHIBA:", shiba+"\n"+"DOGE:",doge+"\n"+"ETH:",eth
      +"\n"+"BitTorrent:",btt+"\n"+"VeChain:",vet+"\n"+"POLYGON:",matic)

