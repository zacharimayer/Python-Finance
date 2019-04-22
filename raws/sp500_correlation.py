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

def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr()
    #print(df_corr.head()) to see some data (it is a lot)

    data = df_corr.values # inner values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) # 1x1 and plot number 1

    heatmap = ax.pcolor(data, cmap=plt.cm.RdBu) # R,Y,G = Red, Yellow, Green. It's a range.
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1) # Limit of the Heatmap (thus colours)
    plt.tight_layout() # Just to clean it more
    plt.show()

visualize_data()
#uncomment to run
