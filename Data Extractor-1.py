import datetime as dt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2000,1,1)
end =dt.datetime(2017,2,28)

df = web.DataReader('SPY', 'yahoo', start, end) #Replace Ticker for Data
df.to_csv('SPDR.csv')  #All of this downloads a Csv file into folder

