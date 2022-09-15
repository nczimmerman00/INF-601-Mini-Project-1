# INF601 - Advanced Programming in Python
# Nicholas Zimmerman
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Request msft ticker data
data = yf.download('MSFT', start='2022-08-30', end='2022-09-14')

# Pulling prices from the ticker data
msftPrices = []

for price in data['Adj Close']:
    msftPrices.append(price)

print(msftPrices)

# Creating numpy array and plotting it
msftArray = np.array(msftPrices)
plt.plot(msftArray)
# Use path instead of the below code
plt.savefig('charts/msft.png')
plt.show()