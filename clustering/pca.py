# PCA
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/clustering/'


# Set 2-Dimension PCA
df=pd.read_csv(path+'NTA.csv',dtype=float,converters={'nta':str})
km=KMeans(n_clusters=4)
df['KM4']=km.fit_predict(df[df.columns[1:]])
p=PCA(n_components=2)
p=pd.DataFrame(data=p.fit_transform(df[df.columns[1:-1]]),columns=['PCA1','PCA2'])
pcakm=KMeans(n_clusters=4)
p['PCA2KM4']=pcakm.fit_predict(p)
df=pd.concat([df,p],axis=1,ignore_index=False)
plt.scatter(df['PCA1'],df['PCA2'],c=df['PCA2KM4'])
df.to_csv(path+'NTAPCA2KM4.csv',index=False)






# Reduce dimensions based on variance
df=pd.read_csv(path+'NTA.csv',dtype=float,converters={'nta':str})
km=KMeans(n_clusters=4)
df['KM4']=km.fit_predict(df[df.columns[1:]])
v=0.99
p=PCA(n_components=v,svd_solver='full')
p.fit_transform(df[df.columns[1:-1]])
k=p.n_components_
p=pd.DataFrame(data=p.fit_transform(df[df.columns[1:-1]]),columns=['PCA'+str(x) for x in range(1,k+1)])
pcakm=KMeans(n_clusters=4)
p['PCAKKM4']=pcakm.fit_predict(p)
df=pd.concat([df,p],axis=1,ignore_index=False)
df.to_csv(path+'NTAPCAKKM4.csv',index=False)



