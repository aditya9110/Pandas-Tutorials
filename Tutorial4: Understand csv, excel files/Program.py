import pandas as pd

# working on .csv file
df = pd.read_csv('stock_data.csv', skiprows=1)  # skips 1st row
print(df)
df = pd.read_csv('stock_data.csv', header=None)  # 1st is not header
print(df)
df = pd.read_csv('stock_data.csv', header=1, names=['tickers', 'eps', 'revenue', 'price', 'people'])
# starts from 2nd row but header=1 as it starts from 0 and headers are provided as names
print(df)
df = pd.read_csv('stock_data.csv', nrows=3)  # print that no of rows
print(df)
df = pd.read_csv('stock_data.csv', na_values=['not available', 'na'])
# replace not available with NaN
print(df)
df = pd.read_csv('stock_data.csv', na_values={
    'eps': ['not available', 'na'],
    'revenue': ['not available', 'na', -1],
    'price': ['not available', 'na'],
    'people': ['not available', 'na']})
# replace data according to the columns and provided in the sub-dict
print(df)

# read to .csv file
df.to_csv('new.csv', index=False, columns=['tickers', 'eps'], header=False)


# working on .excel file
def convert_people_cell(cell):
    if cell == 'na':
        return 'sam walton'
    return cell


def convert_eps_cell(cell):
    if cell == 'not available':
        return None
    return cell


df = pd.read_excel('stock_data.xlsx', converters={
    'people': convert_people_cell,
    'eps': convert_eps_cell})
# use of converters
print(df)

# read to excel file
df.to_excel('new.xlsx', sheet_name='Stocks', startrow=1, startcol=2, index=False)

# read to excel file but to different sheets in same file using function of ExcelWriter class
df_stocks = pd.DataFrame({
    'tickers': ['GOOGLE', 'WMT'],
    'price': [845, 65],
    'eps': [17, 82]
})

df_weather = pd.DataFrame({
    'day': ['1/1/2017', '1/2/2017'],
    'temperature': [32, 35],
    'event': ['Rain', 'Sunny']
})

with pd.ExcelWriter('Stocks_Weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name='Stocks')
    df_weather.to_excel(writer, sheet_name='Weather')
