import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from consumables import Consumables, build_graph
from equipment import Equipment
from reagents import Reagents
from info import Info
from homepage import Homepage

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')])

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/consumables':
        return Consumables()
    if pathname == '/equipment':
        return Equipment()
    if pathname == '/reagents':
        return Reagents()
    if pathname == '/info':
        return Info()
    else:
        return Homepage()
    
@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')])

def update_graph(city):
    graph = build_graph(city)
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
