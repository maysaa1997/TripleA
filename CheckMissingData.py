import pandas as pd
import numpy
import matplotlib.pyplot as plt

df = pd.read_csv("consumption_per_hour.csv")
df_outtemp = pd.read_csv("external_temp_per_hour.csv", index_col='fulldate')
df_intemp = pd.read_csv("internal_temp_per_hour.csv", index_col='fulldate')
df_outhumidity = pd.read_csv("external_humidity_per_hour.csv", index_col='fulldate')
df_inhumidity = pd.read_csv("internal_humidity_per_hour.csv", index_col='fulldate')


print("#################################")

print("Electric Consumption")
print((df['value'] == 0).sum())

print(df.shape)

# mark zero values as missing or NaN
df['value'] = df['value'].replace(0, numpy.NaN)

# drop rows with missing values
df.dropna(inplace=True)

# summarize the number of rows and columns in the dataset
print(df.shape)

print((df['value'] == 0).sum())

###########################################
print("#################################")

print("External Temperature")

print((df_outtemp['external_temp'] == 0).sum())

print(df_outtemp.shape)

# mark zero values as missing or NaN
df_outtemp['external_temp'] = df_outtemp['external_temp'].replace(0, numpy.NaN)

# drop rows with missing values
df_outtemp.dropna(inplace=True)

# summarize the number of rows and columns in the dataset
print(df_outtemp.shape)

print((df_outtemp['external_temp'] == 0).sum())


##################################
print("#################################")

print("Internal Temperature")

print((df_intemp['internal_temp'] == 0).sum())

print(df_intemp.shape)

# mark zero values as missing or NaN
df_intemp['internal_temp'] = df_intemp['internal_temp'].replace(0, numpy.NaN)

# drop rows with missing values
df_intemp.dropna(inplace=True)

# summarize the number of rows and columns in the dataset
print(df_intemp.shape)

print((df_intemp['internal_temp'] == 0).sum())

###################
print("#################################")

print("External Humidity")

print((df_outhumidity['external_humidity'] == 0).sum())

print(df_outhumidity.shape)

# mark zero values as missing or NaN
df_outhumidity['external_temp'] = df_outhumidity['external_humidity'].replace(0, numpy.NaN)

# drop rows with missing values
df_outhumidity.dropna(inplace=True)

# summarize the number of rows and columns in the dataset
print(df_outhumidity.shape)

print((df_outhumidity['external_humidity'] == 0).sum())


print("#################################")

print("Internal Humidity")
print((df_inhumidity['internal_humidity'] == 0).sum())

print(df_inhumidity.shape)

# mark zero values as missing or NaN
df_inhumidity['internal_humidity'] = df_inhumidity['internal_humidity'].replace(0, numpy.NaN)

# drop rows with missing values
df_inhumidity.dropna(inplace=True)

# summarize the number of rows and columns in the dataset
print(df_inhumidity.shape)

print((df_inhumidity['internal_humidity'] == 0).sum())

###################

df.to_csv("consumption_per_hour2.csv")