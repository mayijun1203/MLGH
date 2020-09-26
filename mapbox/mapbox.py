import pandas as pd
import numpy as np
import geopandas as gpd


pd.set_option('display.max_columns', None)
path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/mapbox/'





pt=gpd.read_file(path+'pointtest.geojson')
pt['LatestEntries'].describe(percentiles=np.arange(0.2,1,0.2))
pt['cat']=np.where(pt['LatestEntries']>800,'>800',
          np.where(pt['LatestEntries']>600,'601~800',
          np.where(pt['LatestEntries']>400,'401~600',
          np.where(pt['LatestEntries']>200,'201~400',
          '<=200'))))
pt.to_file(path+'pointtestcat.geojson',driver='GeoJSON',index=True)




ln=gpd.read_file(path+'linetest.geojson')
ln['div'].unique()
ln['cat']=ln['div'].copy()
ln.to_file(path+'linetestcat.geojson',driver='GeoJSON',index=True)





