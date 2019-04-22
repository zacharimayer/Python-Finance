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

def compile_data():
    with open("sp&500tickers.pickle","rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame() # empty for now

    for count, ticker in enumerate(tickers): # enumarate lets you count things
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date',inplace=True)

        df.rename(columns = {'Adj Close':ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'], 1,inplace=True) # 1 is for the axis, returns error if excluded

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer') # how='outer' shows the column even if one ticker does not have a value.

        if count % 10 == 0:
            print(count)

    main_df.head()
    main_df.to_csv('sp500_joined_closes.csv')

compile_data()
#uncomment this to run.

# Check all that Data in the sp500_joined_closes.csv ;)
