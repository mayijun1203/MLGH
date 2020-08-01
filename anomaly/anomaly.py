import pandas as pd  
import numpy as np
import scipy
import sklearn.model_selection
import sklearn.ensemble
import sklearn.cluster
import sklearn.neighbors
import sklearn.covariance
import sklearn.svm
import matplotlib.pyplot as plt



df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/logistic regression/bank.csv',sep=';')
df['deposit']=np.where(df['y']=='yes',1,0)
df=df[['deposit','age','balance']].reset_index(drop=True)

df.plot(x='age',y='balance',s=2,c='deposit',kind='scatter',colorbar=False,colormap='tab20')

clist=np.where(df['deposit']==0,'red','blue')
df.plot(x='age',y='balance',c=clist,kind='scatter',legend=True)

plt.scatter(x=df['age'],y=df['balance'],s=2,c=df['deposit'])

df.plot(x='age',kind='hist')
df.plot(x='balance',kind='kde')
df.plot(x='age',y='balance',kind='scatter')



# Gaussian
# take log or power for skewed data
df['age'].hist(bins=100)
df['balance'].hist(bins=100)
df['agep']=scipy.stats.norm(df['age'].mean(),df['age'].std()).pdf(df['age'])
df['balancep']=scipy.stats.norm(df['balance'].mean(),df['balance'].std()).pdf(df['balance'])
df['p']=df['agep']*df['balancep']
df['a']=np.where(df['p']<=0.0000001,1,0)
df.plot(x='age',y='balance',s=5,c='a',kind='scatter',colorbar=False,colormap='tab20')



# DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
dbscan=sklearn.cluster.DBSCAN(eps=0.2,min_samples=10,metric='euclidean',n_jobs=-1)
df['dbscan']=dbscan.fit_predict(df[['age','balance']])
df.plot(x='age',y='balance',s=5,c='dbscan',kind='scatter',colorbar=False,colormap='tab20')




# Isolation Forest
clf=sklearn.ensemble.IsolationForest(n_estimators=100,warm_start=True)
df['clf']=clf.fit_predict(df[['age','balance']])
df.plot(x='age',y='balance',s=5,c='clf',kind='scatter',colorbar=False,colormap='tab20')




# Local Outlier Factor
lof=sklearn.neighbors.LocalOutlierFactor(n_neighbors=100)
df['lof']=lof.fit_predict(df[['age','balance']])
df.plot(x='age',y='balance',s=5,c='lof',kind='scatter',colorbar=False,colormap='tab20')




# Elliptic Envelope (Multivariate Gaussian distribution)
ee=sklearn.covariance.EllipticEnvelope()
df['ee']=ee.fit_predict(df[['age','balance']])
df.plot(x='age',y='balance',s=5,c='ee',kind='scatter',colorbar=False,colormap='tab20')




# One-Class Support Vector Machines
ocsvm=sklearn.svm.OneClassSVM(kernel='rbf',gamma='scale')
df['ocsvm']=ee.fit_predict(df[['age','balance']])
df.plot(x='age',y='balance',s=5,c='ocsvm',kind='scatter',colorbar=False,colormap='tab20')




















import plotly
import plotly.express as px
plotly.io.renderers.default='browser'
# fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig=px.scatter(x=df['age'],y=df['balance'])
fig.show()
