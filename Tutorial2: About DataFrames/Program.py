import pandas as pd
weather_data={'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017',],
              'temperature':[32,35,28,24,32,31],
              'windspeed':[6,7,2,7,4,2],
              'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']}
df = pd.DataFrame(weather_data) #without .read_csv()
print(df)
rows , cols = df.shape  #dim of table
print(rows)
print(cols)
print(df.head())  #print only few rows at top
print(df.head(2))   #print only top 2 rows
print(df.tail())  #print 5 rows from bottom
print(df.tail(2))   #print only bottom 2 rows
print(df[2:5])
print(df.columns)
print(df.day)
print(df['event'])  #same as df.event
print(df[['event','day']])
print(df['temperature'].max())
print(df.describe())    #prints statistical data on integer cols like mean,min,max,etc

#conditional statements in pandas
print(df[df.temperature>=32])
print(df[df.temperature==df['temperature'].max()])
print(df[['day','temperature']][df.temperature==df['temperature'].max()])

print(df.set_index('day'))  #it wont reflect in original table
df.set_index('day',inplace = True)   #it reflects in original table
print(df)
print(df.loc['1/3/2017'])

df.reset_index(inplace = True)  #to reset with index no
print(df)

df.set_index('event',inplace = True)
print(df)
print(df.loc['Snow'])   #prints all data with events as snow
df.reset_index(inplace = True)
print(df)
