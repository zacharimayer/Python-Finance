import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import datetime, timedelta
import bs4 as bs
import pickle
import requests
import os
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from numpy.core.umath_tests import inner1d

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp&500tickers.pickle","rb") as f: # rb = read bytes
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end = datetime.today()

    for ticker in tickers: # add in [:25] if you want only the first 25 companies
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo',start,end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()
# uncomment to run

# Collecting a lot of Data from Yahoo can take 20-30 minutes
# Therefore storing locally is sometimes _really_ preferred
# THIS CAN TAKE A LOT OF TIME.

# #Wikipedia uses "." instead of "-" in their list. Had to translate "." to "-" so it would get past Berkshire Hathaway. Just for anyone running into this.
# Added this into the initial save_sp500_tickers for loop before it appends the tickers:
# mapping = str.maketrans(".","-")
# ticker = ticker.translate(mapping)
# You will need to delete list file and rerun save_sp500_tickers function.﻿
