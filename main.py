# INF601 - Advanced Programming in Python
# Nicholas Zimmerman
# Mini Project 1

from datetime import datetime, timedelta
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas_market_calendars as mcal

# These are the tickers to be looked up and graphed.
tickers = ['MSFT', 'AAPL', 'IBM', 'GOOGL', 'AMZN']

# Get start and end dates
endDate = datetime.now() - timedelta(days=1)
days = timedelta(days=10)
startDate = endDate - days
endDateString = endDate.strftime("%Y-%m-%d")
startDateString = startDate.strftime('%Y-%m-%d')

# Get market calendar
nyse = mcal.get_calendar('NYSE')
calendar = nyse.schedule(start_date=startDateString, end_date=endDateString)
while calendar.axes[0].size != 11:
    days += timedelta(days=1)
    startDate = endDate - days
    startDateString = startDate.strftime('%Y-%m-%d')
    calendar = nyse.schedule(start_date=startDateString, end_date=endDateString)

# Move back startDate until 10 trading days are present.


for ticker in tickers:
    # Request ticker data
    data = yf.download(ticker, start=startDateString, end=endDateString)

    # Grab ticker closing prices and dates
    dataPrices = []
    dataDates = []
    for price in data['Adj Close']:
        dataPrices.append(price)

    for date in data.axes[0].date:
        dateTimeString = date.strftime('%Y-%m-%d')
        dataDates.append(dateTimeString)

    # Create numpy arrays for the prices and dates and plot it
    priceArray = np.array(dataPrices)
    dateArray = np.array(dataDates)

    # Edit graph settings
    plt.clf()
    plt.title(ticker)
    plt.xlabel('Date')
    plt.ylabel('Price ($) per Share')
    plt.xticks(range(10), dateArray, rotation=60)
    plt.subplots_adjust(bottom=0.25)
    plt.plot(priceArray)

    # Check to make sure the charts directory is created.
    pathString = os.getcwd() + '/charts/'
    if not os.path.exists(pathString):
        os.mkdir(pathString)

    # Save graph in charts folder
    pathString += ticker + '.png'
    plt.savefig(pathString)

exit()
