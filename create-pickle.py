import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()
import pickle
import requests
import fix_yahoo_finance as yf

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find ('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[1].text
        mapping = str.maketrans(".","-")
        ticker = ticker.translate(mapping)
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    return tickers

save_sp500_tickers()
