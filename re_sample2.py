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
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from numpy.core.umath_tests import inner1d

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#The purpose of this script is to resample our data from 1 day to 10 days
df_ohlc = df['Adj Close'].resample('10D').ohlc() #open/high/low/close
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
#df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
print(df_ohlc.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num, df_volume.values, 0))
plt.show()
