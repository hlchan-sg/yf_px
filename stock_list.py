"""
the function within return a stock listing from a worksheet in an excel file
the worksheet must have Ticker as its column head,
the value under this column ('Ticker') will be the stock symbol in each row
"""

### import modules
import pandas as pd

def excel_list(excel_file, sheetname):
    """loads the excel file to be used for pulling data from yfinance"""
    ticker_list = pd.read_excel(excel_file, sheet_name=sheetname).fillna(0)
    print(f"There are total of {len(ticker_list['Ticker'])} stocks in the listing.")
    return ticker_list['Ticker'].apply(lambda x: x.upper())

if __name__ == '__main__':
    main()
