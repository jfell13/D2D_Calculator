import pandas as pd
import pickle
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from navbar import Navbar

nav = Navbar()

header = html.H3(
    'Select the reagents and consumables needed for the D2D class.'
)


# dropdown = html.Div(dcc.Dropdown(
#     id = 'pop_dropdown',
#     #options = options,
#     value = 'Abingdon city, Illinois'
# ))

output = html.Div(id = 'output',
                children = [],)

def Consumables():
    layout = html.Div([
        nav,
        header,
        #dropdown,
        output
    ])
    return layout

def build_graph(city):
    graph = dcc.Graph(
           figure = {
               "data": [{"x": [1, 2, 3], "y": [1, 4, 9]}],
               'layout': go.Layout(
                    title = '{} Population Change'.format(city),
                    yaxis = {'title': 'Population'},
                    hovermode = 'closest')})
    return graph