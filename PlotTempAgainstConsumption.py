import plotly
import plotly.graph_objs as go
import pandas as pd

import plotly.plotly as py


plotly.tools.set_credentials_file(username='MaysaaKHALIL', api_key='JmrWBUCDGdQnC2Eu0fa8')

dataC = pd.read_csv("wholedata.csv", parse_dates=['fulldate'])

trace1 = go.Scatter(
    x=dataC['fulldate'],
    y=dataC['value'],
    name='consumption data'
)

data = [trace1]
layout = go.Layout(
    title='Energy Consumption per hour',
    xaxis=dict(
        title='time'
    ),
    yaxis=dict(
        title='Energy consumption'
    ),

)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='multiple-axes-double')