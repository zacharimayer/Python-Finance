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

def process_data_for_labels(ticker):
    hm_days = 7 # how many days in the future
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1): # If you exclude 1, it starts at 0
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker] # When you shift things, you shift them up or down. Shift negatively, means shifting up.

    df.fillna(0, inplace=True)
    return tickers, df

#process_data_for_labels('XOM')
# Uncomment to test if it works
# We are checking the correlation of years of Data. Correlation thus means (far) less.

def buy_sell_hold(*args): # you can learn more on args on Pythonprorgramming.net
    cols = [c for c in args]
    requirement = 0.02 # means 2%
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0
    # 1 = buy, -1 = sell, 0 = hold

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)]
                                             )) # Can be done better!

    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))
    df.fillna(0, inplace=True)

    df = df.replace([np.inf, -np.inf], np.nan) # Handle for Crazy Values
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change() # Normalized!
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values
    #capital X is Features, y are the Labels

    return X, y, df

#extract_featuresets('ticker') -- specify ticker here

def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,
                                                                        y,
                                                                        test_size = 0.25)
    clf = neighbors.KNeighborsClassifier()

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('Accuracy:', confidence)
    predictions = clf.predict(X_test)
    print('Predicted spread:', Counter(predictions))

    return confidence

do_ml('BAC') # Bank of America

# Average = 0,33. Higher? Outperformance.
# 1 = Buy, -1 = Sell, 0 = Hold
