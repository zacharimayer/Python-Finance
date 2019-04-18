import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)
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

#save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):

    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock.dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2019,4,1)
    end = dt.datetime(2019,4,13)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            data = pdr.get_data_yahoo(ticker, start, end)
            data.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(tickers))
        if ValueError:
            pass  # do nothing!

get_data_from_yahoo()
