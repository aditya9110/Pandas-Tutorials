import pandas as pd
#different ways of creating dataframes

#read from .csv file
df1 = pd.read_csv('weather_data.csv')
print(df1)

#read from .excel file
df2 = pd.read_excel('weather_data.xlsx','Sheet1')
print(df2)

#using py dictionary
weather_data = {'day': ['1/1/2017','1/2/2017','1/3/2017'],
                'temperature': [32,35,28],
                'windspeed': [6,7,2],
                'event': ['Rain', 'Sunny', 'Snow']}
df3 = pd.DataFrame(weather_data)
print(df3)

#using tuples so data provided in list is row to row and in columns
weather_data = [('1/1/2017',32,6,'Rain'),('1/2/2017',35,7,'Sunny'),
                ('1/3/2017',28,2,'Snow')]
#column names or heads are provided here
df4 = pd.DataFrame(data=weather_data,
                  columns=['day','temperature','windspeed','event'])
print(df4)

#using dictionary list where each element represents each row
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},]
df5 = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(df5)
