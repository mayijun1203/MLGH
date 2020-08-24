import pandas as pd  
import numpy as np
import sklearn.model_selection
import sklearn.ensemble



# Classifier
df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/logistic regression/bank.csv',sep=';')
df['deposit']=np.where(df['y']=='yes',1,0)
df['default']=np.where(df['default']=='yes',1,0)
df['housing']=np.where(df['housing']=='yes',1,0)
df['loan']=np.where(df['loan']=='yes',1,0)
df=df[['deposit','age','default','balance','housing','loan','campaign']].reset_index(drop=True)


# Sklearn
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['age','default','balance','housing','loan','campaign']],df['deposit'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)


rf=sklearn.ensemble.RandomForestClassifier().fit(xtrain,ytrain)


ypred=pd.DataFrame({'val':yval,'prob':[x[1] for x in rf.predict_proba(xval)],'pred':rf.predict(xval)})
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


# Sklearn
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['original','age','km','petrol','dealer','manual']],df['sell'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)


rf=sklearn.ensemble.RandomForestRegressor().fit(xtrain,ytrain)
ypred=pd.DataFrame({'val':yval,'pred':rf.predict(xval)})
ypred.plot(x='val',y='pred',style='o')
print(rf.score(xval, yval))

