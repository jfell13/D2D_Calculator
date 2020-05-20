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
    'Information about the D2D Project'
)
body = html.P("""\
The Design to Data (D2d) enzyme course was designed by Justin Siegel and Ashley Vater."""
                           )

# dropdown = html.Div(dcc.Dropdown(
#     id = 'pop_dropdown',
#     #options = options,
#     value = 'Abingdon city, Illinois'
# ))

output = html.Div(id = 'output',
                children = [],)

def Info():
    layout = html.Div([
        nav,
        header,
        body,
        #dropdown,
        output
    ])
    return layout
