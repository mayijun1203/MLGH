import pandas as pd
import plotly.io as pio
import plotly.express as px

pd.set_option('display.max_columns', None)
pio.renderers.default = "browser"
path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/htmlslide/plotly/'



df=pd.read_csv(path+'Subway_ridership_data_20200903.csv')


fig=px.scatter(x=range(10), y=range(10))
fig.show()
fig.write_html(path+'subway.html')
