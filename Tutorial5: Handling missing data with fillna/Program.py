import pandas as pd
df = pd.read_csv('weather_data1.csv')
print(type(df.day[0]))
df = pd.read_csv('weather_data1.csv',parse_dates=['day'])   #change type of day column
print(type(df.day[0]))
df.set_index('day',inplace=True)
print(df)
print(df.fillna(0)) #fill NA with o here but number passed to fillna

new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'no event'
        })
print(new_df)

print(df.fillna(method='ffill'))    #fill missing as next cell
print(df.fillna(method='ffill',limit=1))
#fill missing as next cell but only 1 cell as limit is 1
print(df.fillna(method='bfill'))    #fill missing as previous cell
print(df.fillna(method='bfill',axis='columns'))
#fill missing as previous cell but along columnn and row
print(df.interpolate(method='time'))
#uses linear interpolation or say mean and
#time method is it uses the day column and adjust the missing data

print(df.dropna())  #it will drop the rows with missing data
print(df.dropna(how='all')) #if all data is not available that row is dropped
print(df.dropna(thresh=1))  #atleast 1 valid value 
print(df.dropna(thresh=2))  #atleast 2 valid values

#for missing dates 
dt = pd.date_range('01-01-2017','01-11-2017')
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)    #inplace is not accepted here
#the missing data at the added dates can be filled using above techniques
print(df)
