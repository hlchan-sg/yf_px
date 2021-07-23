"""
This script will download data of a week on the daily 1m prices and save as CSV file compressed using gzip
Note yfinance only downloading of 7 days of 1m data at each scraping run
So it is important to specify the dates to be less than 7 days apart
"""

### import modules
from pathlib import Path
import yfinance as yf
import pandas as pd
import datetime as dt
pd.set_option('display.max_columns', 20, 'display.width', 320, 'display.max_rows', 50)
from stock_list import excel_list


def weekly_day1m(tickers_list, start_date, end_date, raw_dir):
    """
    extract 1m price data including pre and post trading time from yahoo finance based on the given stock listing
    save the data into raw data folder as a gzip csv file (to save space)
    """

    result = []
    for ticker in tickers_list:
        data = yf.download(tickers=ticker, start=start_date, end=end_date, interval='1m',
                           prepost=True, rounding=False, back_adjust=True) # Back-adjusted data to mimic true historical prices
        data.insert(0,'Ticker',ticker)
        data.insert(0, 'DateTime', data.index)
        data['DateTime'] = data['DateTime'].dt.tz_localize(None)
        result.append(data)

    df = pd.concat(result, ignore_index=True)   # .reset_index() adds a new column at [0] with the values being the Data values which is previously the index
    raw_file = Path(raw_dir).joinpath(f'yf_raw_{str(start_date)[:-9]}_{str(end_date)[:-9]}.csv.gz')
    df.to_csv(raw_file, index= False, chunksize=100000, compression='gzip')
    print(f'saved 1m price history to {raw_file}...')
    #return df


### set global variables

# stock list excel file and sheet name
listing_dir = r'C:\Users\Stephen\PycharmProjects\lib\shares'
file = 'master_stock_listing.xlsx'
stock_list = Path(listing_dir).joinpath(file)
sheetname = "atr+mylist"

# data folder
data_dir = r'C:\Users\Stephen\PycharmProjects\lib\shares\data\yf_raw1m'

# date and time for yfinance prices download
"""
yfinance treat time based on our local computer system, ie. NY is 12 hours behind SG time. 
So local datetime at 12 Jun'21 0 hours, ie. 12am Sat (12/6) in SG, it is 12pm Fri (11/6) in NY
to solve this, we need to put 12 hours ahead in the datetime argument, ie. 2021-06-12 12:00:00 SG = 2021-06-12 00:00:00 NY
"""
yf_start = dt.datetime(2021,7,19, 12,0,0)   # must be a monday date, download from EST Monday 12am
yf_end = dt.datetime(2021,7,24, 12,0,0)   # must be a saturday date, download to EST Saturday 12am


def main():
    tickers_list = excel_list(stock_list, sheetname)
    weekly_day1m(tickers_list, yf_start, yf_end, data_dir)


if __name__ == '__main__':
    main()