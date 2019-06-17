import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load data
df = pd.read_csv("consumption_per_day.csv", parse_dates=['fulldate'])

# Group by day and compute the max temp per day
df.index = df['fulldate']


# Identify the day, month and year
df['day'] = df['fulldate'].map(lambda x: x.day)
df['month'] = df['fulldate'].map(lambda x: x.month)
df['year'] = df['fulldate'].map(lambda x: x.year)

# Keep only the data from 2018
df = df[df['year'] == 2018]

# Axis Labels
x = [str(i) for i in range(1,32)]
y = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEPT', 'OCT', 'NOV', 'DEC']


# For each month in 2018, produce an array of 31 values containing the temperature for each day
z = []
for month, group in df.groupby('month'):
    tmp = [0]*31
    for index, row in group.iterrows():
        i = row['day']-1
        tmp[i] = row['value']
    z.append(tmp)

app.layout = html.Div([
    dcc.Graph(
        id='heatmap',
        figure={
            'data': [{
                'z': z,
                'x': x,
                'y': y,
                'type': 'heatmap'
            }]
        }
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('heatmap', 'hoverData'),
     Input('heatmap', 'clickData')])
def display_hoverdata(hoverData, clickData):
    return [
        json.dumps(hoverData, indent=2),
        html.Br(),
        json.dumps(clickData, indent=2)
    ]


if __name__ == '__main__':
    app.run_server(debug=True)