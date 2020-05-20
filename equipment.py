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
    'Select the equipment needed for the D2D class.'
)


# Incubator =  100
# Centrifuge = 1000 
# Vortex = 10

output = html.Div(id = 'output',
                children = [],)

def Equipment():
    layout = html.Div([
        nav,
        header,
        #dropdown,
        output
    ])
    return layout