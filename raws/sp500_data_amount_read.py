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

df = pd.read_csv('sp500_joined_closes.csv')
df.shape

datapoints = 4768 * 506
print("N =",datapoints, "Datapoints")
df.describe()
