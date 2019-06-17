from pandas import Series
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot


# create a difference
def difference(dataset):
    diff = list()
    for i in range(1, len(dataset)):
        value = dataset[i] - dataset[i - 1]
        diff.append(value)
    return Series(diff)

data= pd.read_csv("wholedata.csv")
series = data['value']
X = series.values
X = X.astype('float32')
# difference data
stationary = difference(X)
stationary.index = series.index[1:]
# check if stationary
result = adfuller(stationary)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')

for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))

# plot differenced data
stationary.plot()
pyplot.show()

# save
stationary.to_csv('stationary.csv')