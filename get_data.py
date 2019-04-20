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

start = dt.datetime (2000,1,1)
end = dt.datetime (2019,3,15)
df = web.DataReader('TSLA', 'yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

print(df.tail(10))
