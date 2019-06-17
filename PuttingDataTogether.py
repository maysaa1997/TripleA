import pandas as pd

df_cons = pd.read_csv("consumption_per_hour.csv")
df_outtemp = pd.read_csv("external_temp_per_hour.csv")
df_intemp = pd.read_csv("internal_temp_per_hour.csv")
df_outhumidity = pd.read_csv("external_humidity_per_hour.csv")
df_inhumidity = pd.read_csv("internal_humidity_per_hour.csv")


df_cons.drop("Timestamp", axis=1, inplace=True)

df_outtemp.drop("timestamp", axis=1, inplace=True)

df_intemp.drop("timestamp", axis=1, inplace=True)

#df_inhumidity("timestamp", axis=1, inplace=True)

#df_outhumidity("timestamp", axis=1, inplace=True)

result = pd.concat([df_cons, df_outtemp], axis=1, join='inner')

result2 = pd.concat([df_intemp, df_inhumidity], axis=1, join='inner')

result3 = pd.concat([result2, df_outhumidity], axis=1, join='inner')

result4 = pd.concat([result, result3], axis=1, join='inner')

print(result4)
result4.to_csv("result.csv")
print((result4['external_temp'] == 0).sum())
