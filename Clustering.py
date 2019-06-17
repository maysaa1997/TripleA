import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df = pd.read_csv("consumption_per_hour.csv")

df.drop("fulldate", axis=1, inplace=True)




kmeans = KMeans(n_clusters=12).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['Timestamp'], df['value'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

plt.show()