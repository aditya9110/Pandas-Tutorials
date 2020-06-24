import pandas as pd
df = pd.read_csv('city_weather_p7.csv')
print(df)
g = df.groupby('city')  #grouping by city names and create object
print(g)
#data in form of dict with city as keys and city_df as values
for city,city_df in g:
    print(city)
    print(city_df)

print(g.get_group('mumbai'))  #get data for particular city or key passed as args

print(g.max())  #max of all columns for all cities as 'g' is specified

print(g.describe())

