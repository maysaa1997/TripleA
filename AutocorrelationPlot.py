import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from matplotlib import pyplot

series = pd.read_csv('wholedata.csv')

pyplot.figure()

#pyplot.subplot(211)

#plot_acf(series['value'], ax=pyplot.gca())

#pyplot.subplot(212)

plot_pacf(series['value'], ax=pyplot.gca(), lags=25, title="Partial autocorrelation with lag=25")



pyplot.show()
