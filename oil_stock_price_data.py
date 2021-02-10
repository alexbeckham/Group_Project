import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
yf.pdr_override()

#########################PURPOSE OF THIS CODE###############################
# This code is designed to get the annual stock prices of 4 of the largest oil companies dating back to 1980
# until 2021.
# This will be used to analyze later. 

# Notes.
# Data on some of the stocks really only goes back to 1980. So when you try to do a 5 year moving average. 
# It can't start until 1985


#* PLEASE NOTE THAT I HAD TO SUBSTITUTE DJUSEN FOR XOP AS I COULD NOT FIGURE OUT THE SYMBOL FOR DJUSEN

#########################IMPORTING THE DATA###############################
# Selecting the stocks
stock = [
    'XOM', 
    'CVX',
    'BP',
    'RDS-B'
]
# Creating an empty dataframe to put stuff in
df = pd.DataFrame()

# Putting the stock values into a combined dataframe
for i in stock:
    start = dt.datetime(1975,1,1)
    end = dt.datetime(2021,1,1)
    df[i] = pdr.get_data_yahoo(i,start,end)['Adj Close']

#########################CLEANING THE DATA###############################

# Resetting the index to put the date in a column
df = df.reset_index() #! WORKS: From 1975

# Creating a function that turns the years into strings.
def to_string(x):
    return str(x)

# Taking off the annoying months and dates
df['Date'] = df['Date'].apply(to_string).apply(lambda x: x.split('-')[0]) #! Works: From 1975

# Showing only data from the first day or two of each year.
source_df = df.groupby('Date').first() #! Works: From 175

# Adjusting the column names to match the data
new_column_names = []
for i in source_df:
    new_column_names.append(i + ' Price')

source_df.columns = new_column_names

oil_stock_prices_yearly = source_df[5:]

#########################SETTING THE DATA UP TO BE ANALYZED###############################

# Finding the annual percent changes.
df_change = source_df.pct_change() 


# Adjusting the column names to match the data
df_change.columns = [
    'XOM PCT_CHANGE',
    'CVX PCT_CHANGE',
    'BP PCT_CHANGE',
    'RDS-B PCT_CHANGE'
]

# Finding the 5-year rolling annual percent changes.
df_rolling_change = df_change.rolling(window = 5).mean().dropna()
# Changing the column names to match the new data
df_rolling_change.columns = [
    'XOM ROLLING_PCT_CHANGE',
    'CVX ROLLING_PCT_CHANGE',
    'BP ROLLING_PCT_CHANGE',
    'RDS-B ROLLING_PCT_CHANGE'
]

# Finding the 5-year rolling annual standard deviation 
df_rolling_std = df_change.rolling(window = 5).std().dropna()
df_rolling_std.columns = [
    'XOM ROLLING_STD',
    'CVX ROLLING_STD',
    'BP ROLLING_STD',
    'RDS-B ROLLING_STD'
]
#########################SAVING THE DATA###############################

# oil_stock_prices_yearly.to_csv('oil_stock_prices_every_year_start.csv')
# df_change.to_csv('annual_percent_change.csv')
# df_rolling_change.to_csv('rolling_percent_changes.csv')
# df_rolling_std.to_csv('rolling_std.csv')