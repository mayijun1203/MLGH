import pandas as pd
import itertools as it
import multiprocessing as mp
import numpy as np
import datetime

pd.set_option('display.max_columns', None)
start=datetime.datetime.now()

path='C:/Users/Yijun Ma/Desktop/optimizer/'
#path='/home/mayijun/optimizer/'
#path='E:/optimizer/'

wt=pd.DataFrame({'CAT':['Tactics','Ball Control','Defending','Attacking','Shooting'],'WEIGHT':[2,1,2,2,1]})

df=pd.read_csv(path+'coach.csv')
df=pd.melt(df,id_vars='Name',var_name='CAT',value_name='RATING')

lst=list(df['Name'].unique())
cb1=pd.DataFrame(list(it.combinations(lst,3)))



#def cbgen(cbsplit):
#    for i in cbsplit.index:
#        cb=[]
#        cb2=list(it.combinations([x for x in lst if x not in list(cbsplit.loc[i,:])],3))
#        for j in range(0,len(cb2)):
#            print(j)
#            cb3=list(it.combinations([x for x in lst if x not in list(cbsplit.loc[i,:])+list(cb2[j])],3))
#            for k in range(0,len(cb3)):
#                cb4=list(it.combinations([x for x in lst if x not in list(cbsplit.loc[i,:])+list(cb2[j])+list(cb3[k])],3))
#                for l in range(0,len(cb4)):
#                    cb5=list(it.combinations([x for x in lst if x not in list(cbsplit.loc[i,:])+list(cb2[j])+list(cb3[k])+list(cb4[l])],3))
#                    for m in range(0,len(cb5)):
#                        cb.append(list(cbsplit.loc[i,:])+list(cb2[j])+list(cb3[k])+list(cb4[l])+list(cb5[m]))
#        cb=pd.DataFrame(cb)
#        cb.to_csv(path+'python/'+str(i)+'.csv')



#def parallelize(data, func):
#    data_split = np.array_split(data,mp.cpu_count()-2)
#    pool = mp.Pool(mp.cpu_count()-2)
#    pool.map(func, data_split)
#    pool.close()
#    pool.join()



#if __name__=='__main__':
#    cb1split = np.array_split(cb1,np.ceil(len(cb1)/(mp.cpu_count()-2)))
#    for n in range(0,len(cb1split)):
#        parallelize(cb1split[n], cbgen)
#        print(datetime.datetime.now()-start)



#lp=0
#cball=pd.read_csv(path+'python/'+str(lp)+'.csv')
#cball['NO']=range(len(cball)*lp,len(cball)*(lp+1))
#cball=cball.loc[:,['NO']+[str(x) for x in range(0,15)]]
#cball.to_csv(path+'python/cball.csv',index=False,header=True,mode='w')
#for lp in range(1,len(cb1)):
#    cball=pd.read_csv(path+'python/'+str(lp)+'.csv')
#    cball['NO']=range(len(cball)*lp,len(cball)*(lp+1))
#    cball=cball.loc[:,['NO']+[str(x) for x in range(0,15)]]
#    cball.to_csv(path+'python/cball.csv',index=False,header=False,mode='a')



#def parallelize(data, func):
#    data_split = np.array_split(data,mp.cpu_count()-2)
#    pool = mp.Pool(mp.cpu_count()-2)
#    pool.map(func, data_split)
#    pool.close()
#    pool.join()
#
#
#
#def optrsgen(cballcksplit):
#    opt=pd.DataFrame({'NO':list(np.repeat(cballcksplit['NO'],15)),'CAT':list(np.repeat(df['CAT'].unique(),3))*len(cballcksplit),
#                      'RANK':list(range(1,4))*5*len(cballcksplit),'PICK':cballcksplit.iloc[:,1:].values.flatten()},columns=['NO','CAT','RANK','PICK'])
#    opt=pd.merge(opt,df,how='left',left_on=['PICK','CAT'],right_on=['Name','CAT'],copy=False)
#    opt=opt.drop('Name',axis=1)
#    rs=opt.groupby('NO',as_index=False).filter(lambda x: x['RATING'].min()>0.6)
#    rs=rs.groupby(['NO','CAT'],as_index=False).agg({'RATING':'mean'})
#    rs=rs.groupby('NO',as_index=False).filter(lambda x: x['RATING'].min()>0.65)
#    rs=pd.merge(rs,wt,how='left',on='CAT')
#    rs=rs.groupby('NO',as_index=False).agg({'RATING':lambda x: np.average(x,weights=rs.loc[x.index,'WEIGHT'])}).sort_values('RATING',ascending=False)
#    rs=rs[rs.RATING>0.7]
#    optrs=opt[opt['NO'].isin(rs['NO'].unique())]
#    optrs.to_csv(path+'python/optrs.csv',index=False,header=False,mode='a')
#
#
#
#if __name__=='__main__':
#    cball=pd.read_csv(path+'python/cball.csv',chunksize=1000000)
#    optrsstr=pd.DataFrame(columns=['NO','CAT','RANK','PICK','RATING'])
#    optrsstr.to_csv(path+'python/optrs.csv',index=False,mode='w')
#    for ck in cball:
#        parallelize(ck, optrsgen)



optrs=pd.read_csv(path+'python/optrs.csv')
rs=optrs.groupby(['NO','CAT'],as_index=False).agg({'RATING':'mean'})
rs=pd.merge(rs,wt,how='left',on='CAT')
rs=rs.groupby('NO',as_index=False).agg({'RATING':lambda x: np.average(x,weights=rs.loc[x.index,'WEIGHT'])}).sort_values('RATING',ascending=False)
rs=rs[rs.RATING>0.7313]
optrs=optrs[optrs['NO'].isin(rs['NO'].unique())]
print(optrs)















# Linux set shared variable
#    manager=mp.Manager()
#    optrs=manager.Namespace()
#    optrs.df = pd.DataFrame()