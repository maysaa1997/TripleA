import pandas as pd
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot


data= pd.read_csv("consumption_per_hour.csv")
# q-q plot
qqplot(data['value'], line='s')
pyplot.show()