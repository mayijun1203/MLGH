# K-Means
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import ward,dendrogram

path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/clustering/'

df=pd.read_csv(path+'NTA.csv',dtype=float,converters={'nta':str})


plt.figure()
dendrogram(ward(df[df.columns[1:]]))
plt.show()


agl=AgglomerativeClustering(n_clusters=4)
df['cluster']=agl.fit_predict(df[df.columns[1:]])


