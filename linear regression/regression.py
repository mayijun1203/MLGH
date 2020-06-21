import pandas as pd  
import numpy as np  
import sklearn
import statsmodels.api as sm



df=pd.read_csv('C:/Users/Yijun Ma/Desktop/D/DOCUMENT/GITHUB/MLGH/linear regression/car.csv')
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
ypred=pd.DataFrame({'test':ytest,'pred':reg.predict(xtest)})
print(sklearn.metrics.mean_absolute_error(ytest, ypred['pred']))
print(sklearn.metrics.mean_squared_error(ytest, ypred['pred']))
print(sklearn.metrics.mean_squared_error(ytest, ypred['pred']))
print(sklearn.metrics.median_absolute_error(ytest, ypred['pred']))



# Statsmodels for model summary
sm.OLS(ytrain,sm.add_constant(xtrain)).fit().summary()
