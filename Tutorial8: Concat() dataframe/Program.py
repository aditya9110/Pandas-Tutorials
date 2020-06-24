import pandas as pd
india_weather = pd.DataFrame({
        'city':['mumbai','delhi','banglore'],
        'temp':[32,35,40],
        'humidity':[80,60,70]})
print(india_weather)

usa_weather = pd.DataFrame({
        'city':['new york','calfornia','texas'],
        'temp':[22,25,20],
        'humidity':[50,55,60]})
print(usa_weather)

df = pd.concat([india_weather,usa_weather])
print(df)

df = pd.concat([india_weather,usa_weather],ignore_index=True)
print(df)

#ignore the ingore_index method when using keys
df = pd.concat([india_weather,usa_weather], keys=['india','usa'])
print(df)

print(df.loc['india']) #only data associated with 'india' key

temp_df = pd.DataFrame({
        'city':['mumbai','delhi','banglore'],
        'temp':[32,35,40],}, index=[0,1,2])

humid_df = pd.DataFrame({
        'city':['mumbai','delhi','banglore'],
        'humidity':[80,60,70],}, index=[0,1,2])

df = pd.concat([temp_df,humid_df])
print(df)
#along the column axis to avoid none situation in above output
df = pd.concat([temp_df,humid_df],axis = 1) 
print(df)

#index is  used to align the properly along the columns
humid_df = pd.DataFrame({
        'city':['delhi','mumbai'],
        'humidity':[80,60]},index=[0,1])
df = pd.concat([temp_df,humid_df],axis = 1) 
print(df)

humid_df = pd.DataFrame({
        'city':['delhi','mumbai'],
        'humidity':[80,60]},index=[1,0])
df = pd.concat([temp_df,humid_df],axis = 1) 
print(df)

s = pd.Series(['Humid','Dry','Rain'],name = 'event')
print(s)
df = pd.concat([temp_df,s],axis = 1)
print(df)
