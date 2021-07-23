# yf_px
 simple get started script to download historical stock prices from yahoo finance (either 1 minute 1 day period type). saved file will be in csv or csv gzip type.

#Prerequisite:
1. excel file with a worksheet containing the stocks you wish to download historical prices on. The worksheet must have a column header named 'Ticker' without the quotes.
2. know the directory where you saved this excel file
3. know the name of the worksheet
4. create a folder for the data to be saved into

#How to use:
####Use either yf_px1m (for 1min data) or yf_px1d (for 1day data)

1. change the directory to your own directory in the following:
   
   listing_dir = r'your own directory where excel file is saved'    
   file = 'your excel file.xlsx'    
   sheetname = "the worksheet name containing the stock symbols"
   data_dir = r'your directory to save the historical data'

   
2. change the dates to the period you wanted to download


3. run the script