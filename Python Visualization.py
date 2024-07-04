#!/usr/bin/env python
# coding: utf-8

# # Choropleth Map

# In[1]:


get_ipython().system(' pip install plotly')


# In[2]:


import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ArielZeng/data-science-and-machine-learning-works/main/Choropleth%20Map.csv')
fig = go.Figure(data=go.Choropleth(
 locations = df['CODE'],
 z = df['GDP (BILLIONS)'],
 text = df['COUNTRY'],
 colorscale = 'Viridis', #Inferno, Blues
 autocolorscale=False,
 reversescale=True,
 marker_line_color='darkgray',
 marker_line_width=0.5,
 colorbar_tickprefix = '$',
 colorbar_title = 'GDP<br>Billions US$',
))
fig.update_layout(
 title_text='2014 Global GDP',
 geo=dict(
 showframe=False,
 showcoastlines=False,
 projection_type='equirectangular'
 ),
 annotations = [dict(
 x=0.55,
 y=0.1,
 xref='paper',
 yref='paper',
 text='',
 showarrow = False
 )]
)
fig.show()


# # Bubble Map

# In[4]:


import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ArielZeng/data-science-and-machine-learning-works/main/Bubble%20Map.csv')
df.head()
print (df.head())
df['text'] = df['name'] + '<br>Population ' + (df['pop']/1e6).astype(str)+' million'
limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
cities = []
scale = 5000
fig = go.Figure()
# USA-states
for i in range(len(limits)):
 lim = limits[i]
 df_sub = df[lim[0]:lim[1]]
 fig.add_trace(go.Scattergeo(
 locationmode = 'USA-states',
 lon = df_sub['lon'],
 lat = df_sub['lat'],
 text = df_sub['text'],
 marker = dict(
 size = df_sub['pop']/scale,
 color = colors[i],
 line_color='rgb(40,40,40)',
 line_width=0.5,
 sizemode = 'area'
 ),
 name = '{0} - {1}'.format(lim[0],lim[1])))
fig.update_layout(
 title_text = '....',
 showlegend = True,
 geo = dict(
 scope = 'usa',
 landcolor = 'rgb(217, 217, 217)',
 )
 )
fig.show()


# # Chord Diagram

# In[5]:


get_ipython().system('pip install holoviews hvplot')


# In[11]:


import pandas as pd
import holoviews as hv
from holoviews import opts

hv.extension('bokeh')

# 创建数据矩阵
mymat = pd.DataFrame({
    'A': [0, 3, 12, 6],
    'B': [2, 0, 9, 8],
    'C': [3, 5, 0, 7],
    'D': [4, 9, 6, 0]
}, index=['A', 'B', 'C', 'D'])

# 转换为边列表
edges = mymat.stack().reset_index()
edges.columns = ['source', 'target', 'value']
edges = edges[edges['value'] > 0]  # 移除值为0的连接

# 创建弦图
chord = hv.Chord(edges)
chord.opts(
    opts.Chord(
        labels='index', 
        cmap='Category20', 
        edge_cmap='Category20', 
        edge_color='source',
        width=700,  # 设置图表宽度
        height=700  # 设置图表高度
    )
)

# 显示弦图
chord

