import pandas as pd
from numpy import percentile

data = pd.read_csv("result.csv")

#data.groupby('month')['value'].transform('mean').fillna(0)

#data.loc[data['First Season'] > 1990, 'First Season'] = 1

q25, q75 = percentile(data['value'], 25), percentile(data['value'], 75)
iqr = q75 - q25


# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off

# identify outliers
outliers = [x for x in data['value'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))


data.loc[data['value'] > upper, 'value'] = data['value'].mean()
data.loc[data['value'] < lower, 'value'] = data['value'].mean()


outliers = [x for x in data['value'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))

data.to_csv('resultwithoutoutlier.csv')