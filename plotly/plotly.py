import pandas as pd
import numpy as np
import plotly.io as pio
import plotly.express as px



# pio.renderers.default = "browser"
pd.set_option('display.max_columns', None)


# df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/linear regression/car.csv')
df=pd.read_csv('/home/mayij/GITHUB/MLGH/linear regression/car.csv')
df['sell']=df['Selling_Price']
df['original']=df['Present_Price']
df['age']=2019-df['Year']
df['km']=df['Kms_Driven']/1000
df['petrol']=np.where(df['Fuel_Type']=='Petrol',1,0)
df['dealer']=np.where(df['Seller_Type']=='Dealer',1,0)
df['manual']=np.where(df['Transmission']=='Manual',1,0)
df=df[['sell','original','age','km','petrol','dealer','manual']].reset_index(drop=True)




fig=px.scatter(df,x='original',y='sell')
fig.show()

