import plotly

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
plotly.tools.set_credentials_file(username='MaysaaKHALIL', api_key='JmrWBUCDGdQnC2Eu0fa8')

df0 = pd.read_csv("consumption_per_hour.csv", parse_dates=['fulldate'])
df1 = pd.read_csv("external_temp_per_hour.csv", parse_dates=['fulldate'])
df2 = pd.read_csv("internal_temp_per_hour.csv", parse_dates=['fulldate'])
df3 = pd.read_csv("external_humidity_per_hour.csv", parse_dates=['fulldate'])
df4 = pd.read_csv("internal_humidity_per_hour.csv", parse_dates=['fulldate'])

# Identify the day, month and year
df0['day'] = df0['fulldate'].map(lambda x: x.day)
df0['month'] = df0['fulldate'].map(lambda x: x.month)
df0['year'] = df0['fulldate'].map(lambda x: x.year)



#df0.boxplot(by ='month', column =['value'], grid = False)

sns.set_style("whitegrid")

sns.boxplot(x='month', y='value', data=df0)

#df0.boxplot(column =['value'], grid = False)
plt.show()
