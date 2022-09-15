# INF601 - Advanced Programming in Python
# Nicholas Zimmerman
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from datetime import datetime

# These are the tickers to be looked up and graphed.
tickers = ['MSFT', 'AAPL', 'IBM', 'GOOGL', 'AMZN']

# Set dateFormatter to be used in the xaxis
dateFormatter = mdates.DateFormatter('%Y-%m-%d')

for ticker in tickers:
    # Request ticker data
    data = yf.download(ticker, start='2022-08-30', end='2022-09-14')

    # Grab ticker closing prices and dates
    dataPrices = []
    dataDates = []
    for price in data['Adj Close']:
        dataPrices.append(price)

    for date in data.axes[0].date:
        dataDates.append(date)

    # Create numpy arrays for the prices and dates and plot it
    priceArray = np.array(dataPrices)
    dateArray = np.array(dataDates)

    # Edit graph settings
    plt.clf()
    plt.title(ticker)
    plt.xlabel('Date')
    plt.ylabel('Price ($) per Share')
    plt.xticks(dateArray, rotation=60)
    plt.subplots_adjust(bottom=0.25)
    plt.gca().xaxis.set_major_formatter(dateFormatter)
    plt.plot(dateArray, priceArray)

    # Check to make sure the charts directory is created.
    pathString = os.getcwd() + '/charts/'
    if not os.path.exists(pathString):
        os.mkdir(pathString)

    # Save graph in charts folder
    pathString += ticker + '.png'
    plt.savefig(pathString)

exit()
