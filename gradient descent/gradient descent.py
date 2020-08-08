import pandas as pd  
import numpy as np
import sklearn.model_selection
import sklearn.linear_model
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

df.plot(x='original',y='sell',style='o',title='sell vs original')


xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(df[['original','age','km','petrol','dealer','manual']],df['sell'],test_size=0.2)
xtrain,xval,ytrain,yval=sklearn.model_selection.train_test_split(xtrain,ytrain,test_size=0.25)



moriginal=np.random.randint(0,1)
mage=np.random.randint(0,1)
mkm=np.random.randint(0,1)
mpetrol=np.random.randint(0,1)
mdealer=np.random.randint(0,1)
mmanual=np.random.randint(0,1)
c=np.random.randint(0,10)
a=0.0001
epochs=10000
n=len(xtrain)

for i in range(epochs): 
    ypred=moriginal*xtrain['original']+mage*xtrain['age']+mkm*xtrain['km']+mpetrol*xtrain['petrol']+mdealer*xtrain['dealer']+mmanual*xtrain['manual']+c
    dmoriginal=(-2/n)*sum(xtrain['original']*(ytrain-ypred))
    dmage=(-2/n)*sum(xtrain['age']*(ytrain-ypred))
    dmkm=(-2/n)*sum(xtrain['km']*(ytrain-ypred))
    dmpetrol=(-2/n)*sum(xtrain['petrol']*(ytrain-ypred))
    dmdealer=(-2/n)*sum(xtrain['dealer']*(ytrain-ypred))
    dmmanual=(-2/n)*sum(xtrain['manual']*(ytrain-ypred))
    dc=(-2/n)*sum(ytrain-ypred)
    moriginal=moriginal-a*dmoriginal
    mage=mage-a*dmage
    mkm=mkm-a*dmkm
    mpetrol=mpetrol-a*dmpetrol
    mdealer=mdealer-a*dmdealer
    mmanual=mmanual-a*dmmanual
    c=c-a*dc

print('moriginal:'+str(moriginal)+'\n'+
      'mage:'+str(mage)+'\n'+
      'mkm:'+str(mkm)+'\n'+
      'mpetrol:'+str(mpetrol)+'\n'+
      'mdealer:'+str(mdealer)+'\n'+
      'mmanual:'+str(mmanual)+'\n'+
      'c:'+str(c))



sm.OLS(ytrain,sm.add_constant(xtrain)).fit().summary()
