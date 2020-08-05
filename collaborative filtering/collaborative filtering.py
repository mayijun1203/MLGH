import pandas as pd  
import numpy as np
import sklearn.cluster
import sklearn.decomposition
import surprise






# Memory Based
df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/collaborative filtering/movielens.csv')
df=df.pivot(index='user',columns='item',values='rating').reset_index(drop=False)
df['user']=['U'+str(x) for x in df['user']]
df.columns=['USER']+['M'+str(x) for x in df.columns[1:]]
df=df.replace(np.nan,-1)
v=0.90
p=sklearn.decomposition.PCA(n_components=v,svd_solver='full')
p.fit_transform(df[df.columns[1:]])
print(p.n_components_)
p=pd.DataFrame(data=p.fit_transform(df[df.columns[1:]]),columns=['PCA'+str(x) for x in range(1,p.n_components_+1)])
p=pd.concat([df[['USER']],p],axis=1,ignore_index=False)
dist=pd.DataFrame()
dist['k']=range(1,21)
dist['dist']=np.nan
for k in range(1,21):
    km=sklearn.cluster.KMeans(n_clusters=k)
    km=km.fit(p[p.columns[1:]])
    dist.loc[dist['k']==k,'dist']=km.inertia_
dist.plot(x='k',y='dist')
k=3 # Elbow
km=sklearn.cluster.KMeans(n_clusters=k)
df['CLUSTER']=km.fit_predict(p[p.columns[1:]])+1
df=df.replace(-1,np.nan)
mb=[]
for i in range(1,4):
    tp=df[df['CLUSTER']==i].reset_index(drop=True)
    tpmean=np.mean(tp[tp.columns[1:-1]])
    for j in tp.columns[1:-1]:
        tp[j]=tp[j].replace(np.nan,tpmean[j])
    mb+=[tp]
mb=pd.concat(mb,axis=0,ignore_index=True)





# Model Based
df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/collaborative filtering/movielens.csv')
reader=surprise.Reader(rating_scale=(1, 5))
data=surprise.Dataset.load_from_df(df[['user','item','rating']],reader)
trainset=data.build_full_trainset()


# KNN
algo=surprise.KNNWithMeans(sim_options={'name':'cosine','user_based':False})
algo.fit(trainset)

gs=surprise.model_selection.GridSearchCV(surprise.KNNWithMeans,{'sim_options':{'name':['msd','cosine'],'min_support':[3, 4, 5],'user_based':[False, True]}},measures=['rmse','mae'],cv=3)
gs.fit(data)
print(gs.best_score['rmse'])
print(gs.best_params['rmse'])



# SVD
algo=surprise.SVD(n_epochs=5,lr_all=0.002,reg_all=0.4)
algo.fit(trainset)

gs=surprise.model_selection.GridSearchCV(surprise.SVD,{'n_epochs':[5,10],'lr_all':[0.002,0.005],'reg_all':[0.4,0.6]},measures=['rmse','mae'],cv=3)
gs.fit(data)
print(gs.best_score['rmse'])
print(gs.best_params['rmse'])


algo.predict(100,1)






