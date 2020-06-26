import pandas as pd  
import numpy as np
import sklearn.model_selection
import sklearn.linear_model
import statsmodels.api as sm



df=pd.read_csv('C:/Users/Yijun Ma/Desktop/D/DOCUMENT/GITHUB/MLGH/logistic regression/bank.csv',sep=';')
df['deposit']=np.where(df['y']=='yes',1,0)
df['default']=np.where(df['default']=='yes',1,0)
df['housing']=np.where(df['housing']=='yes',1,0)
df['loan']=np.where(df['loan']=='yes',1,0)
df=df[['deposit','age','default','balance','housing','loan','campaign']].reset_index(drop=True)



# Sklearn
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['age','default','balance','housing','loan','campaign']],df['deposit'],test_size=0.5)
reg=sklearn.linear_model.LogisticRegression().fit(xtrain,ytrain)
ypred=pd.DataFrame({'test':ytest,'prob':[x[1] for x in reg.predict_proba(xtest)],'pred':reg.predict(xtest)})
ypred.plot(x='test',y='pred',style='o')
print(sklearn.metrics.classification_report(ytest, ypred['pred']))



# Statsmodels for model summary
sm.Logit(ytrain,sm.add_constant(xtrain)).fit().summary2()
