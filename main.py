# INF601 - Advanced Programming in Python
# Peyton Meitler
# Mini Project 2

#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from pathlib import Path

# List of stock tickers
stock_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Makes the code run multiple times for multiple stocks
for ticker in stock_tickers:
    # Fetch stock data
    stock = yf.Ticker(ticker)
    hist = stock.history(period="365d") # get historical market data from the past year

    # get the date and closing price
    dates = hist.index
    closing_prices = hist['Close']

    # Makes the trend line
    x = np.arange(len(dates))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, closing_prices)
    trend_line = slope * x + intercept

    # Makes the trendline color red or green based on if its positive or not
    trend_line_color = 'green' if slope > 0 else 'red'

    # Plots all the stuff and adds labels for x and y axis along with a title
    plt.figure(figsize=(10, 6))
    plt.title(f"Closing Price for {ticker} with Trend Line")
    plt.ylabel("Closing Price")
    plt.xlabel("Date")

    # Makes the legend for the graphs
    plt.plot(dates, closing_prices, label="Closing Price", color='blue')
    plt.plot(dates, trend_line, label="Trend Line", color=trend_line_color, linestyle='-')

    # Creates our charts folder
    try:
        # Create charts File
        Path("charts").mkdir()
    except FileExistsError:
        pass
    # Saves the yearly stock graphs to the charts folder
    savefile = f"charts/{ticker}.png"
    plt.savefig(savefile)

    plt.legend()
    plt.grid(True)

    plt.show()




