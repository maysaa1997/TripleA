import pandas as pd


df = pd.read_csv("result.csv", parse_dates=['fulldate'])


df.index = df['fulldate']

df['external_temp'] = df['external_temp'].replace(0, df['external_temp'].mean())


print(df['external_humidity'].describe())




