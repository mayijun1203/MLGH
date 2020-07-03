import pandas as pd  
import numpy as np
import sklearn.model_selection
import sklearn.linear_model
import statsmodels.api as sm



df=pd.read_csv('C:/Users/mayij/Desktop/DOCUMENT/GITHUB/MLGH/linear regression/car.csv')
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
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['original','age','km','petrol','dealer','manual']],df['sell'],test_size=0.5)
reg=sklearn.linear_model.LinearRegression().fit(xtrain,ytrain)
lasso=sklearn.linear_model.Lasso(alpha=0.1).fit(xtrain,ytrain)
ypred=pd.DataFrame({'test':ytest,'pred':reg.predict(xtest),'lasso':lasso.predict(xtest)})
ypred.plot(x='test',y=['pred','lasso'],style='o')
print(sklearn.metrics.mean_absolute_error(ypred['test'], ypred['pred']))
print(sklearn.metrics.mean_absolute_error(ypred['test'], ypred['lasso']))

print(sklearn.metrics.mean_squared_error(ypred['test'], ypred['pred']))
print(sklearn.metrics.mean_squared_error(ypred['test'], ypred['lasso']))

print(sklearn.metrics.mean_squared_error(ypred['test'], ypred['pred']))
print(sklearn.metrics.mean_squared_error(ypred['test'], ypred['lasso']))

print(sklearn.metrics.median_absolute_error(ypred['test'], ypred['pred']))
print(sklearn.metrics.median_absolute_error(ypred['test'], ypred['lasso']))







# Statsmodels for model summary
sm.OLS(ytrain,sm.add_constant(xtrain)).fit().summary()
