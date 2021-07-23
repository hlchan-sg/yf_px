"""
This script will download historical prices, without adjustment for dividends, stock spilt
for a given period and save as CSV file (with the option to save compressed using gzip)
"""

### import modules
from pathlib import Path
import yfinance as yf
import pandas as pd
import datetime as dt
pd.set_option('display.max_columns', 20, 'display.width', 320, 'display.max_rows', 50)
from stock_list import excel_list


def period_1d_csv(tickers_list, start_date, end_date, raw_dir):
    """
    extract 1d daily price data from yahoo finance based on the given ticker list
    save the data into raw data folder as a gzip csv file (to save space)
    """
    try:
        for ticker in tickers_list:
            data = yf.download(tickers=ticker, start=start_date, end=end_date, interval='1d', prepost=True,
                               tz='EST', rounding=False, back_adjust=True) # Back-adjusted data to mimic true historical prices
            data.insert(0,'Ticker',ticker)
            data.insert(0, 'DateTime', data.index)
            data['DateTime'] = data['DateTime'].dt.tz_localize(None)
            raw_file = Path(raw_dir).joinpath(f'raw_{ticker}_{str(start_date)}_{str(end_date)}.csv')
            data.to_csv(raw_file, index=False)
            print(f'Downloaded {(ticker)} stock prices...')
    except Exception as error:
        print(error)


def period_1d_csvGzip(tickers_list, start_date, end_date, raw_dir):
    """
    extract 1d daily price data from yahoo finance based on the given ticker list
    save the data into raw data folder as a csv file
    """
    try:
        for ticker in tickers_list:
            data = yf.download(tickers=ticker, start=start_date, end=end_date, interval='1d', prepost=True,
                               tz='EST', rounding=False, back_adjust=True) # Back-adjusted data to mimic true historical prices
            data.insert(0,'Ticker',ticker)
            data.insert(0, 'DateTime', data.index)
            data['DateTime'] = data['DateTime'].dt.tz_localize(None)
            raw_file = Path(raw_dir).joinpath(f'raw_{ticker}_{str(start_date)}_{str(end_date)}.csv.gz')
            data.to_csv(raw_file, index=False, chunksize=100000, compression='gzip')
            print(f'Downloaded {(ticker)} stock prices...')
    except Exception as error:
        print(error)


### set global variables
# stock list excel file and sheet name
listing_dir = r'C:\Users\Stephen\PycharmProjects\lib\shares'
file = 'master_stock_listing.xlsx'
stock_list = Path(listing_dir).joinpath(file)
sheetname = "atr+mylist"

# data folder
data_dir = r'C:\Users\Stephen\PycharmProjects\lib\shares\data\yf_raw1d'

# date and time for yfinance prices download
yf_start = dt.date(2021,1,1)
yf_end = dt.date(2021,7,17)


def main():
    tickers_list = excel_list(stock_list, sheetname)
    #tickers_list = ['TSLA', 'BYND']
    period_1d_csv(tickers_list, yf_start, yf_end, data_dir)   # save as csv
    period_1d_csvGzip(tickers_list, yf_start, yf_end, data_dir)   # save as csv_gz


if __name__ == '__main__':
    main()