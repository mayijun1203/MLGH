import pandas as pd  
import numpy as np
import sklearn.model_selection
import sklearn.linear_model
import statsmodels.api as sm
import sklearn.ensemble


df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/logistic regression/bank.csv',sep=';')
df['deposit']=np.where(df['y']=='yes',1,0)
df['default']=np.where(df['default']=='yes',1,0)
df['housing']=np.where(df['housing']=='yes',1,0)
df['loan']=np.where(df['loan']=='yes',1,0)
df=df[['deposit','age','default','balance','housing','loan','campaign']].reset_index(drop=True)




# Gaussian first
# take log or power for skewed data


# Isolation Forest
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['age','default','balance','housing','loan','campaign']],df['deposit'],test_size=0.2)
clf=sklearn.ensemble.IsolationForest(n_estimators=100,warm_start=True).fit(xtrain)

ypred=pd.DataFrame({'train':ytrain,'pred':clf.fit_predict(xtrain)})

ypred.plot(x='val',y='pred',style='o')
print(sklearn.metrics.classification_report(yval, ypred['pred']))







import plotly
import plotly.express as px
plotly.io.renderers.default = "browser"
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
