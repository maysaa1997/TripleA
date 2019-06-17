# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



toto = [54.117065, 5.615079, 33.72931, 1.172040, 1.043717, 4.392679, 0.973824]
x_values = ["Electric Consumption(t-1)", "External Temperature(t)", "External Humidity(t)", "Wind Direction(t)", "Shortwave Radiation(t)", "Wind Speed(t)"]
app.layout = html.Div(children=[


    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x_values, 'y': toto, 'type': 'bar', 'name': 'Impact'},

            ],
            'layout': {
                'title': 'Impact of each Input Variable on Energy Consumption(t)'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)