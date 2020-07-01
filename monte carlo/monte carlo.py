import pandas as pd
import numpy as np

tp=[]
for i in range(0,10000):
    target=np.random.choice(a=[75,100,200,300,400,500],size=500,p=[0.3,0.3,0.2,0.1,0.05,0.05])
    ptarget=np.random.normal(loc=1,scale=0.1,size=500).round(2)
    df=pd.DataFrame({'target':target,'ptarget':ptarget})
    df['sales']=df['target']*df['ptarget']
    df['comrate']=np.where(df['ptarget']<=0.9,20,np.where(df['ptarget']<=0.99,30,40))
    df['com']=df['sales']*df['comrate']
    tp+=[[sum(df['target']),sum(df['sales']),sum(df['com'])/1000]]
tp=pd.DataFrame(tp,columns=['target','sales','com'])
tp.hist('com',bins=100)