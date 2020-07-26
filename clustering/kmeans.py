# K-Means
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/clustering/'

df=pd.read_csv(path+'NTA.csv',dtype=float,converters={'nta':str})
dist=pd.DataFrame()
dist['k']=range(1,10)
dist['dist']=np.nan
for k in range(1,10):
    km=KMeans(n_clusters=k)
    km=km.fit(df[df.columns[1:]])
    dist.loc[dist['k']==k,'dist']=km.inertia_
plt.plot(dist['k'],dist['dist'])
k=4 # Elbow
km=KMeans(n_clusters=k)
y=km.fit_predict(df[df.columns[1:]])
df['cluster']=y
df.to_csv(path+'NTAKM4.csv',index=False)


