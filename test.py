import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
from pathlib import Path
yf.pdr_override()
pd.set_option('display.width',None)

temp = pd.read_csv()
stock = [
    'PLUG', 
    'ENPH',
    'DQ',
    'VER',
    'ORA',
    'MEL',
    'SGRE',
    'FSLR',
]
# start = dt.datetime(1975,1,1)
# end = dt.datetime(2021,1,1)
# df = pdr.get_data_yahoo(stock,start,end)['Adj Close']
# print(df)