import pandas as pd
import numpy as np

df = pd.read_csv('weather_data_p6.csv')
print(df)

df1 = df.replace([-99999,-88888],np.NaN)    #replace using list of content
print(df1)

df2 = df.replace({'temperature': -99999,
                  'windspeed': -99999,
                  'event': 0},np.NaN)
print(df2)  #replace col by col using dict

df3 = df.replace({-99999:np.NaN,-88888:np.NaN,'0':'Snow'})
print(df3)

#replace using regex or patterns
df4 = df.replace({7:'7 mph',32:'32 F'})
print(df4.replace('[A-Za-z]','',regex=True))
df4 =df4.replace({'temperature':'[A-Za-z]',
                  'windspeed':'[A-Za-z]'},'',regex=True)
print(df4)

#replace by providing both list and mapping it with each other
df = pd.DataFrame({
        'score':['exceptional','avg','good','poor','exceptional'],
        'student':['rob','maya','parth','tom','amy']})
print(df)
df = df.replace(['poor','avg','good','exceptional'],[1,2,3,4])
print(df)
