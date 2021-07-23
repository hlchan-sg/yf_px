import numpy as np
import pandas as pd
import requests
import yfinance as yf
#from stock_list import excel_list


def get_symbol(stocks):
    df = pd.DataFrame(stocks)
    df.columns=['Ticker']
    return df['Ticker'].apply(lambda x: x.upper())

z = ['aapl', 'TSLA']
y = get_symbol(z)
print(y)