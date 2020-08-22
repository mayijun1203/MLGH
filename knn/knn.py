import pandas as pd  
import numpy as np
import sklearn.model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor


# Classification
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












# Regression
df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/linear regression/car.csv')
df['sell']=df['Selling_Price']
df['original']=df['Present_Price']
df['age']=2019-df['Year']
df['km']=df['Kms_Driven']/1000
df['petrol']=np.where(df['Fuel_Type']=='Petrol',1,0)
df['dealer']=np.where(df['Seller_Type']=='Dealer',1,0)
df['manual']=np.where(df['Transmission']=='Manual',1,0)
df=df[['sell','original','age','km','petrol','dealer','manual']].reset_index(drop=True)


xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['original','age','km','petrol','dealer','manual']],df['sell'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)


score=pd.DataFrame()
score['k']=range(1,21)
score['trainscore']=np.nan
score['valscore']=np.nan
for i in list(score['k']):
    knn=KNeighborsRegressor(n_neighbors=i).fit(xtrain,ytrain)
    score.loc[score['k']==i,'trainscore']=knn.score(xtrain,ytrain)
    score.loc[score['k']==i,'valscore']=knn.score(xval,yval)

k=11
knn=KNeighborsRegressor(n_neighbors=k).fit(xtrain,ytrain)

ypred=pd.DataFrame({'test':ytest,'pred':knn.predict(xtest)})
ypred.plot(x='test',y=['pred'],style='o')









