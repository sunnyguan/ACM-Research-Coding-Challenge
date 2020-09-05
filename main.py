import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# reads in the csv file
data = pd.read_csv('ClusterPlot.csv')

# used for testing the input csv file
# plt.scatter(data["V1"], data["V2"])
# plt.show()

# calculates the total distance from centroid for each point
def elbow(points, kmax):
    sse = {}
    for k in range(1, kmax+1):
        kmeans = KMeans(n_clusters=k).fit(points)
        centroids = kmeans.cluster_centers_
        sse[k] = kmeans.inertia_
    return sse

# copies the data to run elbow on
x = data.copy()
sse = elbow(x, 10)
print(sse)

# graphing result
plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel("Clusters")
plt.ylabel("Total Distance")
plt.show()