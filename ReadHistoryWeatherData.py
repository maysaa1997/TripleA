import pandas as pd

data = pd.read_csv("historyweatherdata.csv", sep=';', encoding='utf8')



result = pd.read_csv("resultwithoutoutlier.csv")


data.drop("Year", axis=1, inplace=True)
data.drop("Month", axis=1, inplace=True)
data.drop("Day", axis=1, inplace=True)
data.drop("Hour", axis=1, inplace=True)
data.drop("Minute", axis=1, inplace=True)

result2 = pd.concat([result, data], axis=1, join='inner')


result2.rename(index=str, columns={"Total Precipitation (high resolution)  [sfc]": "Total Precipitation", "Snowfall Amount (high resolution)  [sfc]": "Snowfall Amount", "Total Cloud Cover  [sfc]": "Total Cloud Cover", "Sunshine Duration  [sfc]": "Sunshine Duration", "Shortwave Radiation  [sfc]": "Shortwave Radiation", "Wind Speed  [10 m above gnd]": "Wind Speed", "Wind Direction  [10 m above gnd]": "Wind Direction"}, inplace=True)
print(list(result2))


result2.to_csv('wholedata.csv')