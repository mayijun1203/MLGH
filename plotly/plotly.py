import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as ps
import json


pd.set_option('display.max_columns', None)
pio.renderers.default = "browser"
path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/plotly/'
mapboxtoken=pd.read_table(path+'mapboxtoken.txt',header=None).loc[0,0]









# Testing
df=pd.read_csv(path+'Subway_ridership_data_20200903.csv')
df=df[::-1].reset_index(drop=True)
df['% Change From 2019']=[pd.to_numeric(x.replace('%',''))/100 for x in df['% Change From 2019 Weekday/Saturday/Sunday Average']]


fig=px.bar(df,x='Date', y='Total Estimated Ridership')
# fig.update_layout(autosize=True)
# fig.show()
fig.write_html(path+'subway.html')




fig=px.scatter(df,x='Date', y='Total Estimated Ridership',color='% Change From 2019',
               title='<b>TEST<b>',template='plotly_white')
fig.update_layout(
    yaxis_fixedrange=True,
    xaxis_fixedrange=True,
    dragmode=False
)
fig.write_html(path+'subway.html',include_plotlyjs='cdn')





gdf=pd.read_csv(path+'cplxam.csv')
fig=px.scatter_mapbox(gdf,lat='CplxLat',lon='CplxLong',color='LatestEntries',
                  color_continuous_scale=px.colors.carto.Teal_r,
                  mapbox_style="carto-positron")
fig.update_layout(
    mapbox=dict(
        bearing=0,
        center=dict(
            lat=40.765735,
            lon=-73.978331
        ),
        zoom=9.5,
        )
)
fig.show()
fig.write_html(path+'turnstile.html',include_plotlyjs='cdn')
fig.write_html('C:/Users/mayij/Desktop/DOC/GITHUB/td-covid19/report/plotly/turnstile.html',include_plotlyjs='cdn')


gdf=pd.read_csv(path+'cplxam.csv')
fig=px.scatter_mapbox(gdf,lat='CplxLat',lon='CplxLong',color='LatestEntries',
                      color_continuous_scale=px.colors.carto.Teal_r)
fig.update_layout(
    mapbox_style="light",
    mapbox_accesstoken=mapboxtoken,
    mapbox_zoom=9.5,
    mapbox_center={"lat": 40.765735, "lon": -73.978331})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
fig.write_html(path+'turnstile.html',include_plotlyjs='cdn')
fig.write_html('C:/Users/mayij/Desktop/DOC/GITHUB/td-covid19/report/plotly/turnstile.html',include_plotlyjs='cdn')




















# Mapping Full Settings
# Point
# px.set_mapbox_access_token(mapboxtoken)
df=pd.read_csv(path+'cplxam.csv')
df['DiffPct1'].describe(percentiles=np.arange(0.2,1,0.2))
df['cat']=np.where(df['DiffPct1']>=-0.9,'>=-90%',
          np.where(df['DiffPct1']>=-0.92,'-92%~-91%',
          np.where(df['DiffPct1']>=-0.94,'-94%~-93%',
          np.where(df['DiffPct1']>=-0.96,'-96%~-95%',
          '<-96%'))))
fig=px.scatter_mapbox(df,
                      lat='CplxLat',
                      lon='CplxLong',
                      color='cat',
                      # text='Borough',
                      hover_name='CplxName',
                      hover_data={'CplxName':True,
                                  'CplxLat':False,
                                  'CplxLong':False,
                                  'Percent Change':(':.2f',df['DiffPct1']),
                                  'Percent Change Category':df['cat'],
                                  'cat':True},
                      # size=range(0,426),
                      category_orders={'cat':['>=-90%','-92%~-91%','-94%~-93%','-96%~-95%','<-96%']},
                      labels={'cat':'Percent Change Category'},
                      color_discrete_sequence=['#d1e3f3','#9ac8e1','#529dcc','#1c6cb1','#08306b'],
                      # color_discrete_map={'-94%~-93%':'#7f2704'},
                      opacity=0.9,
                      size_max=10,
                      zoom=9.5,
                      center={'lat':np.mean(df['CplxLat']),'lon':np.mean(df['CplxLong'])},
                      mapbox_style='carto-positron',
                      title='Mapping Full Settings',
                      template='ggplot2',
                      # height=800,
                      width=800)
fig.show()
fig.write_html(path+'cplxam.html',include_plotlyjs='cdn')




# Line
import json
gdf=pd.read_json(path+'subway_line.geojson')
points = []
for  feature in gdf['features']:
    if feature['geometry']['type'] == 'Polygon':
        points.extend(feature['geometry']['coordinates'][0])    
        points.append([None, None]) # mark the end of a polygon   
        
    elif feature['geometry']['type'] == 'MultiPolygon':
        for polyg in feature['geometry']['coordinates']:
            points.extend(polyg[0])
            points.append([None, None]) #end of polygon
    elif feature['geometry']['type'] == 'LineString': 
        points.extend(feature['geometry']['coordinates'])
        points.append([None, None])
    elif feature['geometry']['type'] == 'MultiLineString':
        for line  in feature['geometry']['coordinates']:
            points.extend(line)
            points.append([None, None])
    else: pass  
lons, lats = zip(*points)
fig=px.line_mapbox(
            lat=lats,
            lon=lons,
        )
fig.show()


gdf=gpd.read_file(path+'subway_line.geojson')
gdf['geometry']=[x[0] for x in gdf['geometry']]
gdf['lat']=[x.xy[1] for x in gdf['geometry']]
gdf['lon']=[x.xy[0] for x in gdf['geometry']]
fig=px.line_mapbox(gdf,
                   lat='lat',
                   lon='lon')
fig.show()












# Polygon
px.set_mapbox_access_token(mapboxtoken)
gdf=gpd.read_file(path+'cplxpknta.shp')
gdf['PKDiffPct3'].describe(percentiles=np.arange(0.2,1,0.2))
gdf['cat']=np.where(gdf['PKDiffPct3']>=4,'>=400%',
           np.where(gdf['PKDiffPct3']>=3,'300%~399%',
           np.where(gdf['PKDiffPct3']>=2,'200%~299%',
           np.where(gdf['PKDiffPct3']>=1,'100%~199%',
           '<100%'))))
# gdf.to_file(path+'cplxpknta.geojson',driver='GeoJSON',index=True)
# gdf=gpd.read_file(path+'cplxpknta.geojson')
gjs=json.loads(gdf.to_json())
fig=px.choropleth_mapbox(data_frame=gdf,
                         geojson=gjs,
                         # featureidkey='properties.NTAName',
                         locations='NTAName',
                         color='cat',
                         hover_name='NTAName',
                         hover_data={'index':False,
                                     'Percent Change':(':.2f',gdf['PKDiffPct3']),
                                     'cat':False},
                         category_orders={'cat':['<100%','100%~199%','200%~299%','300%~399%','>=400%']},
                         labels={'cat':'Percent Change Category'},
                         color_discrete_sequence=['#d1e3f3','#9ac8e1','#529dcc','#1c6cb1','#08306b'],
                         center={'lat':np.mean([min(gdf.bounds['miny']),max(gdf.bounds['maxy'])]),
                                 'lon':np.mean([min(gdf.bounds['minx']),max(gdf.bounds['maxx'])])},
                         zoom=9.5,
                         mapbox_style='carto-positron',
                         title='Polygon',
                         template='ggplot2',
                         height=800,
                         width=800
                         )
fig.show()
fig.write_image(path+'cplxpknta.jpg',
                width=800,
                height=800,
                scale=1,
                validate=True,
                engine='kaleido')
fig.write_html(path+'cplxpknta.html',include_plotlyjs='cdn')


