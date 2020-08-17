# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:54:42 2019

@author: Y_Ma2
"""

import datetime
import geopandas as gpd
import pandas as pd
import numpy as np
import dask.dataframe as dd

#path='E:/TRAVELSHEDREVAMP/'
path='/home/mayijun/TRAVELSHED/'




#start=datetime.datetime.now()
#
## block
## allstation
#allstationlist=pd.read_excel(path+'edc/edc3/location3.xlsx',sheet_name='allstation',dtype=str)
#df=dd.read_csv(path+'edc/allstationworkwtbk.csv',dtype=str)
#allstation=df[['blockid']+list(allstationlist['siteid'])]
#
## nyctract
#nyctractlist=pd.read_excel(path+'edc/edc3/location3.xlsx',sheet_name='nyctract',dtype=str)
#df=dd.read_csv(path+'edc/nyctractworkbk.csv',dtype=str)
#nyctract=df[['blockid']+list(['WORK36047'+x[1:7] for x in nyctractlist['siteid']])]
#nyctract.columns=['blockid']+list(nyctractlist['siteid'])
#
## regionalrail
#regionalraillist=pd.read_excel(path+'edc/edc3/location3.xlsx',sheet_name='regionalrail',dtype=str)
#df=dd.read_csv(path+'edc/regionalworkwtbk.csv',dtype=str)
#regionalrail=df[['blockid']+list(regionalraillist['siteid'])]
#
## edc
#edc=allstation.merge(regionalrail,on='blockid')
#edc=edc.merge(nyctract,on='blockid')
#edc=edc.compute()
#
#ddtime=datetime.datetime.now()-start
#print(ddtime)
#659 secs
#1050 secs


start=datetime.datetime.now()

# block
# allstation
allstationlist=pd.read_excel(path+'edc/edc3/location3.xlsx',sheet_name='allstation',dtype=str)
allstation=pd.DataFrame(columns=['blockid']+list(allstationlist['siteid']),dtype=str)
rd=pd.read_csv(path+'edc/allstationworkwtbk.csv',dtype=str,chunksize=100000)
for ck in rd:
    df=ck[['blockid']+list(allstationlist['siteid'])]
    allstation=allstation.append(df,ignore_index=True)

# nyctract
nyctractlist=pd.read_excel(path+'edc/edc3/location3.xlsx',sheet_name='nyctract',dtype=str)
nyctract=pd.DataFrame(columns=['blockid']+list(nyctractlist['siteid']),dtype=str)
rd=pd.read_csv(path+'edc/nyctractworkbk.csv',dtype=str,chunksize=100000)
for ck in rd:
    df=ck[['blockid']+list(['WORK36047'+x[1:7] for x in nyctractlist['siteid']])]
    df.columns=['blockid']+list(nyctractlist['siteid'])
    nyctract=nyctract.append(df,ignore_index=True)

# regionalrail
regionalraillist=pd.read_excel(path+'edc/edc3/location3.xlsx',sheet_name='regionalrail',dtype=str)
regionalrail=pd.DataFrame(columns=['blockid']+list(regionalraillist['siteid']),dtype=str)
rd=pd.read_csv(path+'edc/regionalworkwtbk.csv',dtype=str,chunksize=100000)
for ck in rd:
    df=ck[['blockid']+list(regionalraillist['siteid'])]
    regionalrail=regionalrail.append(df,ignore_index=True)

# edc
edc=allstation.merge(regionalrail,on='blockid')
edc=edc.merge(nyctract,on='blockid')

pdtime=datetime.datetime.now()-start
print(pdtime)

#480 secs
#628 secs




