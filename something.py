import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
yf.pdr_override()

#! This code will bring in the stock data of 2 ETFs going back to 1980-present.
#* PLEASE NOTE THAT I HAD TO SUBSTITUTE DJUSEN FOR XOP AS I COULD NOT FIGURE OUT THE SYMBOL FOR DJUSEN

# Selecting the stocks
stock = ['XOM', 'CVX','BP','RDS-B']

df = pd.DataFrame()

# Putting the stock values into a combined dataframe
for i in stock:
    start = dt.datetime(1980,1,1)
    end = dt.datetime(2021,1,1)
    df[i] = pdr.get_data_yahoo(i,start,end)['Adj Close']

df = df.reset_index()

# Creating a function that turns the years into strings.
def to_string(x):
    return str(x)

# Taking off the annoying months and dates
df['Date'] = df['Date'].apply(to_string).apply(lambda x: x.split('-')[0])

# Showing only data from the first day or two of each year.
oil_stock_prices_yearly = df.groupby('Date').first()
print(oil_stock_prices_yearly)
oil_stock_prices_yearly.to_csv('oil_stock_prices_every_year_start.csv')
        