import pandas as pd
import geopandas as gpd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go


pd.set_option('display.max_columns', None)
pio.renderers.default = "browser"
path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/plotly/'
mapboxtoken=pd.read_table(path+'mapboxtoken.txt',header=None).loc[0,0]


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


