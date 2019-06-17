
# identify outliers with interquartile range
import pandas as pd
from numpy import percentile


data = pd.read_csv("consumption_per_hour.csv")

# calculate interquartile range
q25, q75 = percentile(data['value'], 25), percentile(data['value'], 75)
iqr = q75 - q25
print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
# identify outliers
outliers = [x for x in data['value'] if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data['value'] if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))