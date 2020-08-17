import pandas as pd
import itertools as it
import numpy as np
import datetime

pd.set_option('display.max_columns', None)
start=datetime.datetime.now()

path='C:/Users/mayij/Desktop/fm/'

wt=pd.DataFrame({'CAT':['Tactics','Ball Control','Defending','Attacking','Shooting'],'WEIGHT':[2,1,2,2,1]})

df=pd.read_csv(path+'coach.csv')
df=pd.melt(df,id_vars='Name',var_name='CAT',value_name='RATING')




start=datetime.datetime.now()

fm=pd.DataFrame(columns=range(0,15))
fm.to_csv(path+'fm.csv',index=False,header=True,mode='w')
lst=list(df['Name'].unique())
cb1=list(it.combinations(lst,3))
cb2=[a+b for a,b in it.product(cb1,cb1)]
cb2=[x for x in cb2 if len(set(x))==6]
# for i in range(0,len(cb2)):
for i in range(0,200):
    print(i)
    k=cb2[i]
    k=[a+b for a,b in it.product([k],cb1)]
    k=[x for x in k if len(set(x))==9]
    k=[a+b for a,b in it.product(k,cb1)]
    k=[x for x in k if len(set(x))==12]
    k=[a+b for a,b in it.product(k,cb1)]
    k=[x for x in k if len(set(x))==15]
    k=pd.DataFrame(k)
    k.to_csv(path+'fm.csv',index=False,header=False,mode='a')

print(datetime.datetime.now()-start)

100100/100*60/60/60
100100/200*70



