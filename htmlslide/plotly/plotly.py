import pandas as pd
import plotly.io as pio
import plotly.express as px

pd.set_option('display.max_columns', None)
pio.renderers.default = "browser"
path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/htmlslide/plotly/'



df=pd.read_csv(path+'Subway_ridership_data_20200903.csv')
df['Date']=df[::-1].reset_index(drop=True)


fig=px.bar(df,x='Date', y='Total Estimated Ridership')
fig.update_layout(autosize=True)
# fig.show()
fig.write_html(path+'subway.html')
