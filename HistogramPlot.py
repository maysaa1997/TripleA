# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("consumption_per_hour2.csv", parse_dates=['fulldate'])
df['day'] = df['fulldate'].map(lambda x: x.day)
df['month'] = df['fulldate'].map(lambda x: x.month)
df['year'] = df['fulldate'].map(lambda x: x.year)
df = df[df['year'] == 2018]

app.layout = html.Div(children=[


    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['month'], 'y': df['value'], 'type': 'bar', 'name': 'Energy consumption per hour'},

            ],
            'layout': {
                'title': 'Energy Consumption per hour grouped by month'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)