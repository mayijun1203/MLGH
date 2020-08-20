import pandas as pd  
import numpy as np
import sklearn.model_selection
from sklearn.neighbors import KNeighborsClassifier



df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/logistic regression/bank.csv',sep=';')
df['deposit']=np.where(df['y']=='yes',1,0)
df['default']=np.where(df['default']=='yes',1,0)
df['housing']=np.where(df['housing']=='yes',1,0)
df['loan']=np.where(df['loan']=='yes',1,0)
df=df[['deposit','age','default','balance','housing','loan','campaign']].reset_index(drop=True)




xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['age','default','balance','housing','loan','campaign']],df['deposit'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)


pd.plotting.scatter_matrix(xtrain,c=ytrain,marker='o',s=10,hist_kwds={'bins':20},figsize=(12,12))



knn=KNeighborsClassifier(n_neighbors=5).fit(xtrain,ytrain)


ypred=pd.DataFrame({'val':ytrain,'prob':[x[1] for x in knn.predict_proba(xtrain)],'pred':knn.predict(xtrain)})
ypred=pd.DataFrame({'val':yval,'prob':[x[1] for x in knn.predict_proba(xval)],'pred':knn.predict(xval)})

ypred.plot(x='val',y='pred',style='o')
print(sklearn.metrics.classification_report(yval, ypred['pred']))















