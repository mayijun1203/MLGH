import pandas as pd
import geopandas as gpd
import json
import numpy as np
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.io as pio
import plotly.graph_objects as go

pio.renderers.default="browser"
pd.set_option('display.max_columns',None)

app=Dash('__main__')

gdf=gpd.read_file('C:/Users/mayij/Desktop/test.geojson')
gdf.crs=4326
gjs=json.loads(gdf.to_json())

fig=go.Figure()
fig=fig.add_trace(go.Choroplethmapbox(name='test',
                                      geojson=gjs,
                                       featureidkey='properties.tractid',
                                      locations=gdf['tractid'],
                                      z=gdf['chinese'],
                                      colorscale="Viridis"))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_center={'lat':np.mean([min(gdf.bounds['miny']),max(gdf.bounds['maxy'])]),
                                 'lon':np.mean([min(gdf.bounds['minx']),max(gdf.bounds['maxx'])])},
                  mapbox_zoom=9)



app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    dcc.Graph(
        id='map',
        figure=fig
    ),
    
    html.Div(children=[
        html.P('Click Data'),
        html.Br(),
        html.P(id='click-data')
    ])
])

@app.callback(
    Output('click-data', 'children'),
    Input('map', 'clickData'))
def display_click_data(clickData):
    try:
        return str(clickData['points'][0]['z'])
    except:
        return 0

# k='{"points": [{"curveNumber": 0, "pointNumber": 1413, "pointIndex": 1413, "location": "36047050300", "z": 32, "bbox": {"x0": 522.1301317530742, "x1": 522.1301317530742, "y0": 309.76902464902327, "y1": 309.76902464902327}}]}'
# json.loads(k)['points'][0]['z']

if __name__ == '__main__':
    app.run_server(debug=True)
