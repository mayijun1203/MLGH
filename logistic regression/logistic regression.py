import pandas as pd  
import numpy as np
import sklearn.model_selection
import sklearn.linear_model
import statsmodels.api as sm



df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/logistic regression/bank.csv',sep=';')
df['deposit']=np.where(df['y']=='yes',1,0)
df['default']=np.where(df['default']=='yes',1,0)
df['housing']=np.where(df['housing']=='yes',1,0)
df['loan']=np.where(df['loan']=='yes',1,0)
df=df[['deposit','age','default','balance','housing','loan','campaign']].reset_index(drop=True)



# Sklearn
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['age','default','balance','housing','loan','campaign']],df['deposit'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)
reg=sklearn.linear_model.LogisticRegression().fit(xtrain,ytrain)
ypred=pd.DataFrame({'val':yval,'prob':[x[1] for x in reg.predict_proba(xval)],'pred':reg.predict(xval)})
ypred.plot(x='val',y='pred',style='o')
print(sklearn.metrics.classification_report(yval, ypred['pred']))



# Statsmodels for model summary
sm.Logit(ytrain,sm.add_constant(xtrain)).fit().summary2()















df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/IPFGH/HHTS.csv')
df['SEX']=np.where(df['SEX']=='MALE',1,0)
df['RACE1']=np.where(df['RACE']=='BLACK',1,0)
df['RACE2']=np.where(df['RACE']=='ASIAN',1,0)
df['RACE3']=np.where(df['RACE']=='OTHER',1,0)
df['AGE1']=np.where(df['AGE']=='A25-34',1,0)
df['AGE2']=np.where(df['AGE']=='A35-54',1,0)
df['AGE3']=np.where(df['AGE']=='A55-64',1,0)
df['AGE4']=np.where(df['AGE']=='A>=65',1,0)
df['EMP']=np.where(df['EMPLY']=='Yes',1,0)
df['TRIP']=np.where(df['PTRIPS']==1,1,np.where(df['PTRIPS']==2,2,np.where(df['PTRIPS']==3,3,np.where(df['PTRIPS']==4,4,5))))
df=df[['SEX','RACE1','RACE2','RACE3','AGE1','AGE2','AGE3','AGE4','EMP','TRIP']].reset_index(drop=True)

xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['SEX','RACE1','RACE2','RACE3','AGE1','AGE2','AGE3','AGE4','EMP']],df['TRIP'],test_size=0.4)

reg=sklearn.linear_model.LogisticRegression().fit(xtrain,ytrain)
ypred=pd.DataFrame({'test':ytest,'pred':reg.predict(xtest)})
sm.MNLogit(ytrain,sm.add_constant(xtrain)).fit().summary()



