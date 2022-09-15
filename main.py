# INF601 - Advanced Programming in Python
# Nicholas Zimmerman
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

tickers = ['MSFT', 'AAPL', 'IBM', 'GOOGL', 'AMZN']

for ticker in tickers:
    # Request ticker data
    data = yf.download(ticker, start='2022-08-30', end='2022-09-14')

    # Grab ticker closing prices
    dataPrices = []
    for price in data['Adj Close']:
        dataPrices.append(price)

    # Create numpy array and plot it
    dataArray = np.array(dataPrices)
    plt.plot(dataArray)

    # Check to make sure the charts directory is created.
    pathString = os.getcwd() + '/charts/'
    if not os.path.exists(pathString):
        os.mkdir(pathString)

    # Save graph in charts folder
    pathString += ticker + '.png'
    plt.savefig(pathString)
