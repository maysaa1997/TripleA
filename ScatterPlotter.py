import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv("consumption_per_hour2.csv", parse_dates=['fulldate'])
df['day'] = df['fulldate'].map(lambda x: x.day)
df['month'] = df['fulldate'].map(lambda x: x.month)
df['year'] = df['fulldate'].map(lambda x: x.year)
df = df[df['year'] == 2018]

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['month'] == i]['fulldate'],
                    y=df[df['month'] == i]['value'],
                    text=df[df['month'] == i]['value'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=str(i)
                ) for i in df.month.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'date', 'title': 'datetime'},
                yaxis={'title': 'Consumption per hour by month'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)