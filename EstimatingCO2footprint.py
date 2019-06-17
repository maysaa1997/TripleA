import pandas as pd

data = pd.read_csv("consumption_per_day.csv")

data['carbonfootprint'] = data['value'] * 41 / 907185

print(data)

data.to_csv('consumption_per_day2.csv')
