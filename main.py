# INF601 - Advanced Programming in Python
# Peyton Meitler
# Mini Project 2

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# gets information on whatever stock you enter
stock = yf.Ticker("AAPL")
hist = stock.history(period="365d") # get historical market data from the past year

# Extract the date and closing price
dates = hist.index
closing_prices = hist['Close']

# Calculate the trend line
x = np.arange(len(dates))
slope, intercept, r_value, p_value, std_err = stats.linregress(x, closing_prices)
trend_line = slope * x + intercept

# Determine the color of the trend line based on its slope
trend_line_color = 'green' if slope > 0 else 'red'

# Plot the closing price and trend line
plt.figure(figsize=(10, 6))
plt.title("Closing Price for Microsoft (MSFT) with Trend Line")
plt.ylabel("Closing Price")
plt.xlabel("Date")

plt.plot(dates, closing_prices, label="Closing Price", color='blue')
plt.plot(dates, trend_line, label="Trend Line", color=trend_line_color, linestyle='-')

plt.legend()
plt.grid(True)

plt.show()




