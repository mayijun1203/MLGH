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




















# Plotly Express

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
                         featureidkey='properties.NTAName',
                         locations='NTAName',
                         color='cat',
                         hover_name='NTAName',
                         hover_data={'NTAName':False,
                                     'cat':False,
                                     'Percent Change':(':.2f',gdf['PKDiffPct3'])},
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










# Plotly Graph Objects
gdf=gpd.read_file(path+'cplxpknta.shp')
gdf['PKDiffPct3'].describe(percentiles=np.arange(0.2,1,0.2))
gdf['cat']=np.where(gdf['PKDiffPct3']>=4,'>=400%',
           np.where(gdf['PKDiffPct3']>=3,'300%~399%',
           np.where(gdf['PKDiffPct3']>=2,'200%~299%',
           np.where(gdf['PKDiffPct3']>=1,'100%~199%',
           '<100%'))))
gjs=json.loads(gdf.to_json())

fig=go.Figure()
fig.add_trace(
    go.Choropleth(
        geojson=gjs,
        featureidkey='properties.NTACode',
        locations=gdf.loc[gdf['cat']=='>=400%','NTACode'],
        z=gdf['PKDiffPct3'],
        colorscale=['#d1e3f3','#9ac8e1','#529dcc','#1c6cb1','#08306b'],
        marker_line_color='#FFFFFF'))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=9.5,
                  mapbox_center={'lat':np.mean([min(gdf.bounds['miny']),max(gdf.bounds['maxy'])]),
                                 'lon':np.mean([min(gdf.bounds['minx']),max(gdf.bounds['maxx'])])})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()









# Line Chart
df=pd.read_csv(path+'pedcounts.csv')
dfcolors={'Weekday AM Peak':'rgba(255,158,74,0.8)',
          'Weekday PM Peak':'rgba(173,139,201,0.8)',
          'Saturday Midday':'rgba(103,191,92,0.8)'}
fig=go.Figure()
fig=fig.add_trace(go.Scatter(name='',
                             mode='none',
                             x=df['Year'],
                             y=df['Weekday AM Peak'],
                             showlegend=False,
                             hovertext=['<b>Year: </b>'+str(x) for x in df['Year']],
                             hoverinfo='text'))
for i in ['Weekday AM Peak','Weekday PM Peak','Saturday Midday']:
    fig=fig.add_trace(go.Scatter(name=i,
                                 mode='lines+markers',
                                 x=df['Year'],
                                 y=df[i],
                                 line={'color':dfcolors[i],
                                       'width':2},
                                 marker = {'color': dfcolors[i],
                                           'size': 6},
                                 hovertext=['<b>'+str(i)+': </b>'+'{:,.0f}'.format(x) for x in df[i]],
                                 hoverinfo='text'))
fig.update_layout(
    template='plotly_white',
    title={'text':'<b>Average Peak Hour Pedestrian Counts</b>',
           'font_size':20,
           'x':0.5,
           'xanchor':'center',
           'y':0.95,
           'yanchor':'top'},
    legend={'orientation':'h',
            'title_text':'',
            'font_size':16,
            'x':0.5,
            'xanchor':'center',
            'y':1,
            'yanchor':'bottom'},
    margin={'b':120,
            'l':80,
            'r':40,
            't':120},
    xaxis={'title':{'text':'<b>Year</b>',
                    'font_size':14},
           'tickfont_size':12,
           'dtick':'M12',
           'range':[min(df['Year'])-0.5,max(df['Year'])+0.5],
           'fixedrange':True,
           'showgrid':False},
    yaxis={'title':{'text':'<b>Hourly Total</b>',
                    'font_size':14},
           'tickfont_size':12,
           'rangemode':'tozero',
           'fixedrange':True,
           'showgrid':True},
    hoverlabel={'font_size':14},
    font={'family':'Arial',
          'color':'black'},
    dragmode=False,
    hovermode='x unified')
fig.add_annotation(
    text='Data Source: <a href="https://data.ny.gov/Transportation/Bi-Annual-Pedestrian-Counts/2de2-6x2h/about" target="blank">NYC DOT</a> | <a href="https://raw.githubusercontent.com/NYCPlanning/td-trends/main/peds/pedcounts.csv" target="blank">Download Chart Data</a>',
    font_size=14,
    showarrow=False,
    x=1,
    xanchor='right',
    xref='paper',
    y=0,
    yanchor='top',
    yref='paper',
    yshift=-80)
fig.write_html(path+'linechart.html',
               include_plotlyjs='cdn',
               config={'displayModeBar':False})






# Stacked Bar Chart
df=pd.read_csv(path+'pedcounts.csv')
dfcolors={'Weekday AM Peak':'rgba(255,158,74,0.8)',
          'Weekday PM Peak':'rgba(173,139,201,0.8)',
          'Saturday Midday':'rgba(103,191,92,0.8)'}
fig=go.Figure()
for i in ['Weekday AM Peak','Weekday PM Peak','Saturday Midday']:
    fig=fig.add_trace(go.Bar(name=i,
                             x=df['Year'],
                             y=df[i],
                             marker = {'color': dfcolors[i]},
                             width=0.5,
                             hovertext=['<b>'+str(i)+': </b>'+'{:,.0f}'.format(x) for x in df[i]],
                             hoverinfo='text'))
fig=fig.add_trace(go.Scatter(name='',
                         mode='none',
                         x=df['Year'],
                         y=df['Weekday AM Peak'],
                         showlegend=False,
                         hovertext=['<b>Year: </b>'+str(x) for x in df['Year']],
                         hoverinfo='text'))
fig.update_layout(
    barmode='stack',
    template='plotly_white',
    title={'text':'<b>Average Peak Hour Pedestrian Counts</b>',
           'font_size':20,
           'x':0.5,
           'xanchor':'center',
           'y':0.95,
           'yanchor':'top'},
    legend={'orientation':'h',
            'title_text':'',
            'font_size':16,
            'x':0.5,
            'xanchor':'center',
            'y':1,
            'yanchor':'bottom'},
    margin={'b':120,
            'l':80,
            'r':40,
            't':120},
    xaxis={'title':{'text':'<b>Year</b>',
                    'font_size':14},
           'tickfont_size':12,
           'dtick':'M12',
           'range':[min(df['Year'])-0.5,max(df['Year'])+0.5],
           'fixedrange':True,
           'showgrid':False},
    yaxis={'title':{'text':'<b>Hourly Total</b>',
                    'font_size':14},
           'tickfont_size':12,
           'rangemode':'tozero',
           'fixedrange':True,
           'showgrid':True},
    hoverlabel={'font_size':14},
    font={'family':'Arial',
          'color':'black'},
    dragmode=False,
    hovermode='x unified')
fig.add_annotation(
    text='Data Source: <a href="https://data.ny.gov/Transportation/Bi-Annual-Pedestrian-Counts/2de2-6x2h/about" target="blank">NYC DOT</a> | <a href="https://raw.githubusercontent.com/NYCPlanning/td-trends/main/peds/pedcounts.csv" target="blank">Download Chart Data</a>',
    font_size=14,
    showarrow=False,
    x=1,
    xanchor='right',
    xref='paper',
    y=0,
    yanchor='top',
    yref='paper',
    yshift=-80)
fig.write_html(path+'stackedbarchart.html',
               include_plotlyjs='cdn',
               config={'displayModeBar':False})





# Fill Chart
df=pd.read_csv(path+'pedcounts.csv')
dfcolors={'Weekday AM Peak':'rgba(255,158,74,0.6)',
          'Weekday PM Peak':'rgba(173,139,201,0.6)',
          'Saturday Midday':'rgba(103,191,92,0.6)'}
fig=go.Figure()
for i in ['Weekday AM Peak','Weekday PM Peak','Saturday Midday']:
    fig=fig.add_trace(go.Scatter(name=i,
                                 x=df['Year'],
                                 y=df[i],
                                 mode = 'none',
                                 stackgroup = 'one',
                                 groupnorm = '',
                                 orientation = 'v',
                                 fill = 'tonexty',
                                 fillcolor = dfcolors[i],
                                 hovertext=['<b>'+str(i)+': </b>'+'{:,.0f}'.format(x) for x in df[i]],
                                 hoverinfo='text'))
fig=fig.add_trace(go.Scatter(name='',
                         mode='none',
                         x=df['Year'],
                         y=df['Weekday AM Peak'],
                         showlegend=False,
                         hovertext=['<b>Year: </b>'+str(x) for x in df['Year']],
                         hoverinfo='text'))
fig.update_layout(
    template='plotly_white',
    title={'text':'<b>Average Peak Hour Pedestrian Counts</b>',
           'font_size':20,
           'x':0.5,
           'xanchor':'center',
           'y':0.95,
           'yanchor':'top'},
    legend={'orientation':'h',
            'title_text':'',
            'font_size':16,
            'x':0.5,
            'xanchor':'center',
            'y':1,
            'yanchor':'bottom'},
    margin={'b':120,
            'l':80,
            'r':40,
            't':120},
    xaxis={'title':{'text':'<b>Year</b>',
                    'font_size':14},
           'tickfont_size':12,
           'dtick':'M12',
           'range':[min(df['Year'])-0.5,max(df['Year'])+0.5],
           'fixedrange':True,
           'showgrid':False},
    yaxis={'title':{'text':'<b>Hourly Total</b>',
                    'font_size':14},
           'tickfont_size':12,
           'rangemode':'tozero',
           'fixedrange':True,
           'showgrid':True},
    hoverlabel={'font_size':14},
    font={'family':'Arial',
          'color':'black'},
    dragmode=False,
    hovermode='x unified')
fig.add_annotation(
    text='Data Source: <a href="https://data.ny.gov/Transportation/Bi-Annual-Pedestrian-Counts/2de2-6x2h/about" target="blank">NYC DOT</a> | <a href="https://raw.githubusercontent.com/NYCPlanning/td-trends/main/peds/pedcounts.csv" target="blank">Download Chart Data</a>',
    font_size=14,
    showarrow=False,
    x=1,
    xanchor='right',
    xref='paper',
    y=0,
    yanchor='top',
    yref='paper',
    yshift=-80)
fig.write_html(path+'fillchart.html',
               include_plotlyjs='cdn',
               config={'displayModeBar':False})







# Two Axis Chart
df=pd.read_csv(path+'pedcounts.csv')
dfcolors={'Weekday AM Peak':'rgba(255,158,74,0.6)',
          'Weekday PM Peak':'rgba(173,139,201,0.6)',
          'Saturday Midday':'rgba(103,191,92,0.8)'}
fig=go.Figure()
for i in ['Weekday AM Peak','Weekday PM Peak']:
    fig=fig.add_trace(go.Scatter(name=i,
                                 x=df['Year'],
                                 y=df[i],
                                 mode = 'none',
                                 stackgroup = 'one',
                                 groupnorm = '',
                                 orientation = 'v',
                                 fill = 'tonexty',
                                 fillcolor = dfcolors[i],
                                 hovertext=['<b>'+str(i)+': </b>'+'{:,.0f}'.format(x) for x in df[i]],
                                 hoverinfo='text'))
fig=fig.add_trace(go.Scatter(name='Saturday Midday',
                         mode='lines',
                         x=df['Year'],
                         y=df['Saturday Midday'],
                         yaxis='y2',
                         showlegend=False,
                         line={'color':dfcolors['Saturday Midday'],
                               'width':3},
                         hovertext=['<b>Saturday Midday: </b>'+str(x) for x in df['Saturday Midday']],
                         hoverinfo='text'))
fig=fig.add_trace(go.Scatter(name='',
                         mode='none',
                         x=df['Year'],
                         y=df['Weekday AM Peak'],
                         showlegend=False,
                         hovertext=['<b>Year: </b>'+str(x) for x in df['Year']],
                         hoverinfo='text'))
fig.update_layout(
    template='plotly_white',
    title={'text':'<b>Average Peak Hour Pedestrian Counts</b>',
           'font_size':20,
           'x':0.5,
           'xanchor':'center',
           'y':0.95,
           'yanchor':'top'},
    legend={'orientation':'h',
            'title_text':'',
            'font_size':16,
            'x':0.5,
            'xanchor':'center',
            'y':1,
            'yanchor':'bottom'},
    margin={'b':120,
            'l':80,
            'r':40,
            't':120},
    xaxis={'title':{'text':'<b>Year</b>',
                    'font_size':14},
           'tickfont_size':12,
           'dtick':'M12',
           'range':[min(df['Year'])-0.5,max(df['Year'])+0.5],
           'fixedrange':True,
           'showgrid':False},
    yaxis={'title':{'text':'<b>Hourly Total</b>',
                    'font_size':14},
           'tickfont_size':12,
           'rangemode':'tozero',
           'fixedrange':True,
           'showgrid':True},
    yaxis2={'title':{'text':'<b>Saturday</b>',
                 'font_size':14},
        'tickfont_size':12,
        'side':'right',
        'overlaying':'y',
        'rangemode':'tozero',
        'fixedrange':True,
        'showgrid':False},
    hoverlabel={'font_size':14},
    font={'family':'Arial',
          'color':'black'},
    dragmode=False,
    hovermode='x unified')
fig.add_annotation(
    text='Data Source: <a href="https://data.ny.gov/Transportation/Bi-Annual-Pedestrian-Counts/2de2-6x2h/about" target="blank">NYC DOT</a> | <a href="https://raw.githubusercontent.com/NYCPlanning/td-trends/main/peds/pedcounts.csv" target="blank">Download Chart Data</a>',
    font_size=14,
    showarrow=False,
    x=1,
    xanchor='right',
    xref='paper',
    y=0,
    yanchor='top',
    yref='paper',
    yshift=-80)
fig.write_html(path+'twoaxischart.html',
               include_plotlyjs='cdn',
               config={'displayModeBar':False})






# Pie Chart
df=pd.read_csv(path+'pedcounts.csv')
df=df.loc[[0]]
df=df.melt(id_vars='Year',value_vars=['Weekday AM Peak','Weekday PM Peak','Saturday Midday'])
df['pct']=df['value']/sum(df['value'])
dfcolors={'Weekday AM Peak':'rgba(255,158,74,0.8)',
          'Weekday PM Peak':'rgba(173,139,201,0.8)',
          'Saturday Midday':'rgba(103,191,92,0.8)'}
fig = go.Figure()
fig = fig.add_trace(go.Pie(labels = df['variable'],
                           values = df['pct'],
                           hole = 0.5,
                           sort = False,
                           direction = 'clockwise',
                           pull=0.05,
                           marker = {'colors': list(dfcolors.values())},
                           textinfo = 'text',
                           text= df['pct'].map('{:.0%}'.format),
                           textposition='outside',
                           textfont={'size':14},
                           hoverinfo = 'text',
                           hovertext = '<b>Type: </b>'+ df['variable'] + '<br><b>Counts: </b>' + df['value'].map('{:,.0f}'.format) +'<br><b>Percentage: </b>' + df['pct'].map('{:.0%}'.format)))
fig.update_layout(template = 'plotly_white',
                  title = {'text': '<b>Micromobility Peak Hour Sample Counts<b>',
                           'font_size': 20,
                           'x': .5,
                           'xanchor': 'center',
                           'y': .95,
                           'yanchor': 'top'},
                  legend = {'traceorder': 'normal',
                            'orientation': 'h',
                            'font_size': 16,
                            'x': .5,
                            'xanchor': 'center',
                            'y': 1,
                            'yanchor': 'bottom'},
                  margin = {'b': 40, 
                            'l': 80,
                            'r': 80,
                            't': 200},
                  hoverlabel = {'font_size': 14}, 
                  font = {'family': 'Arial',
                          'color': 'black'},
                  dragmode = False)
fig.add_annotation(text = 'Data Source: NYC DCP (2021) | <a href="https://raw.githubusercontent.com/NYCPlanning/td-trends/main/micromobility/micromobility.csv" target="blank">Download Chart Data</a>',
                   font_size = 14,
                   showarrow = False, 
                   x = 1, 
                   xanchor = 'right',
                   xref = 'paper',
                   y=0,
                   yanchor='top',
                   yref='paper',
                   yshift=0)
fig
fig.write_html(path + 'piechart.html', include_plotlyjs='cdn', config={'displayModeBar':False})





# Subplot
df=pd.read_csv(path+'pedcounts.csv')
dfcolors={'Weekday AM Peak':'rgba(255,158,74,0.8)',
          'Weekday PM Peak':'rgba(173,139,201,0.8)',
          'Saturday Midday':'rgba(103,191,92,0.8)'}
fig = ps.make_subplots(rows = 1,
                       cols = 3,
                       shared_yaxes = True,
                       subplot_titles = ['Weekday AM Peak','Weekday PM Peak','Saturday Midday'])
for i in df['Year']:
    fig = fig.add_trace(go.Bar(name = i,
                                x = [0],
                                y = df.loc[df['Year']==i,'Weekday AM Peak'],
                                legendgroup = i,
                                showlegend = True),
                        row = 1,
                        col = 1)    
for i in range(1,3):
    for j in df['Year']:
        fig = fig.add_trace(go.Bar(name = ['Weekday AM Peak','Weekday PM Peak','Saturday Midday'][i],
                                    x = [0],
                                    y = df.loc[df['Year']==j,['Weekday AM Peak','Weekday PM Peak','Saturday Midday'][i]],
                                    legendgroup = j,
                                    showlegend = False),
                            row = 1,
                            col = i+1)    
fig.update_layout(
    barmode='stack',
    template='plotly_white',
    title={'text':'<b>Average Peak Hour Pedestrian Counts</b>',
           'font_size':20,
           'x':0.5,
           'xanchor':'center',
           'y':0.95,
           'yanchor':'top'},
    legend={'orientation':'h',
            'title_text':'',
            'font_size':16,
            'x':0.5,
            'xanchor':'center',
            'y':1,
            'yanchor':'bottom'},
    margin={'b':120,
            'l':80,
            'r':40,
            't':120},
    xaxis={'fixedrange':True,
           'showgrid':False},
    yaxis={'title':{'text':'<b>Hourly Total</b>',
                    'font_size':14},
           'tickfont_size':12,
           'rangemode':'tozero',
           'fixedrange':True,
           'showgrid':True},
    hoverlabel={'font_size':14},
    font={'family':'Arial',
          'color':'black'},
    dragmode=False)
for i in range(0,3):
    fig.layout.annotations[i].update(y = 0, 
                                     yanchor = 'top',
                                     yref = 'paper',
                                     yshift = -40,
                                     text = '<b>' + ['Weekday AM Peak','Weekday PM Peak','Saturday Midday'][i] + '</b>',
                                     font = {'size': 14,
                                             'family': 'Arial'})
fig.add_annotation(
    text='Data Source: <a href="https://data.ny.gov/Transportation/Bi-Annual-Pedestrian-Counts/2de2-6x2h/about" target="blank">NYC DOT</a> | <a href="https://raw.githubusercontent.com/NYCPlanning/td-trends/main/peds/pedcounts.csv" target="blank">Download Chart Data</a>',
    font_size=14,
    showarrow=False,
    x=1,
    xanchor='right',
    xref='paper',
    y=0,
    yanchor='top',
    yref='paper',
    yshift=-80)
fig.write_html(path+'subplot.html',
               include_plotlyjs='cdn',
               config={'displayModeBar':False})













