import pandas as pd  
import numpy as np
import sklearn.model_selection
import sklearn.linear_model
import sklearn.preprocessing
import statsmodels.api as sm



df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/linear regression/car.csv')
df['sell']=df['Selling_Price']
df['original']=df['Present_Price']
df['age']=2019-df['Year']
df['km']=df['Kms_Driven']/1000
df['petrol']=np.where(df['Fuel_Type']=='Petrol',1,0)
df['dealer']=np.where(df['Seller_Type']=='Dealer',1,0)
df['manual']=np.where(df['Transmission']=='Manual',1,0)
df=df[['sell','original','age','km','petrol','dealer','manual']].reset_index(drop=True)



# Plot
df.plot(x='original',y='sell',style='o',title='sell vs original')



# Sklearn
# Split and Scale
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['original','age','km','petrol','dealer','manual']],df['sell'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)

scalar=sklearn.preprocessing.MinMaxScaler().fit(xtrain)
xtrainscaled=scalar.transform(xtrain)
xvalscaled=scalar.transform(xval)
xtestscaled=scalar.transform(xtest)



# Linear Regression
reg=sklearn.linear_model.LinearRegression().fit(xtrainscaled,ytrain)
print('Train set R-Squared: '+str(reg.score(xtrainscaled,ytrain)))
ypred=pd.DataFrame({'val':yval,'pred':reg.predict(xvalscaled)})
ypred.plot(x='val',y='pred',style='o')
print('Val set R-Squared: '+str(reg.score(xvalscaled,yval)))
ypred=pd.DataFrame({'test':ytest,'pred':reg.predict(xtestscaled)})
ypred.plot(x='test',y='pred',style='o')
print('Test set R-Squared: '+str(reg.score(xtestscaled,ytest)))



# Ridge Regression
score=pd.DataFrame()
score['a']=[0.1,0.2,0.5,1,2,5,10,20,50,100]
score['trainscore']=np.nan
score['valscore']=np.nan
for i in list(score['a']):
    ridge=sklearn.linear_model.Ridge(alpha=i).fit(xtrainscaled,ytrain)
    score.loc[score['a']==i,'trainscore']=ridge.score(xtrainscaled,ytrain)
    score.loc[score['a']==i,'valscore']=ridge.score(xvalscaled,yval)
a=1
ridge=sklearn.linear_model.Ridge(alpha=a).fit(xtrainscaled,ytrain)
print('Train set R-Squared: '+str(ridge.score(xtrainscaled,ytrain)))
ypred=pd.DataFrame({'val':yval,'pred':ridge.predict(xvalscaled)})
ypred.plot(x='val',y='pred',style='o')
print('Val set R-Squared: '+str(ridge.score(xvalscaled,yval)))
ypred=pd.DataFrame({'test':ytest,'pred':ridge.predict(xtestscaled)})
ypred.plot(x='test',y='pred',style='o')
print('Test set R-Squared: '+str(ridge.score(xtestscaled,ytest)))



# Lasso Regression
score=pd.DataFrame()
score['a']=[0.01,0.05,0.1,0.2,0.5,1,2]
score['trainscore']=np.nan
score['valscore']=np.nan
for i in list(score['a']):
    lasso=sklearn.linear_model.Lasso(alpha=i).fit(xtrainscaled,ytrain)
    score.loc[score['a']==i,'trainscore']=lasso.score(xtrainscaled,ytrain)
    score.loc[score['a']==i,'valscore']=lasso.score(xvalscaled,yval)
a=0.1
lasso=sklearn.linear_model.Lasso(alpha=a).fit(xtrainscaled,ytrain)
print('Train set R-Squared: '+str(lasso.score(xtrainscaled,ytrain)))
ypred=pd.DataFrame({'val':yval,'pred':lasso.predict(xvalscaled)})
ypred.plot(x='val',y='pred',style='o')
print('Val set R-Squared: '+str(lasso.score(xvalscaled,yval)))
ypred=pd.DataFrame({'test':ytest,'pred':lasso.predict(xtestscaled)})
ypred.plot(x='test',y='pred',style='o')
print('Test set R-Squared: '+str(lasso.score(xtestscaled,ytest)))



# Compare
ypred=pd.DataFrame({'test':ytest,'reg':reg.predict(xtestscaled),'ridge':ridge.predict(xtestscaled),'lasso':lasso.predict(xtestscaled)})
ypred.plot(x='test',y=['reg','ridge','lasso'],style='o')
print('Test set Reg R-Squared: '+str(reg.score(xtestscaled,ytest)))
print('Test set Ridge R-Squared: '+str(ridge.score(xtestscaled,ytest)))
print('Test set Lasso R-Squared: '+str(lasso.score(xtestscaled,ytest)))







# Statsmodels for model summary
sm.OLS(ytrain,sm.add_constant(xtrain)).fit().summary()



