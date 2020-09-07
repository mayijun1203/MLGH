import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go


pd.set_option('display.max_columns', None)
pio.renderers.default = "browser"
path='C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/htmlslide/plotly/'



df=pd.read_csv(path+'Subway_ridership_data_20200903.csv')
df=df[::-1].reset_index(drop=True)
df['% Change From 2019']=[pd.to_numeric(x.replace('%',''))/100 for x in df['% Change From 2019 Weekday/Saturday/Sunday Average']]


fig=px.bar(df,x='Date', y='Total Estimated Ridership')
# fig.update_layout(autosize=True)
# fig.show()
fig.write_html(path+'subway.html')




fig=px.scatter(df,x='Date', y='Total Estimated Ridership',color='% Change From 2019',title='<b>TEST<b>')
fig.update_layout(
    font_family="sans-serif",
)
fig.show()
