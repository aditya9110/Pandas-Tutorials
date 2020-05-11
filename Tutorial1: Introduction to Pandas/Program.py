import pandas as pd
df = pd.read_csv('C:\\Users\\aditya\\Downloads\\nyc_weather_report.csv')
print(df)
print(df['Temperature'].max())  #max in temp column
print(df['EST'][df['Events']=='Rain'])  #dates on which event was rain
df.fillna(0, inplace = True)
#replaces the blank spaces with 0 or called data wrangling
print(df['WindSpeedMPH'].mean())
