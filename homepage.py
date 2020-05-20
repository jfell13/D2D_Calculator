import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from navbar import Navbar
from threading import Timer
import webbrowser

nav = Navbar()

body = dbc.Container(
    [dbc.Row(
        [dbc.Col(
            [html.H2("D2D Cost Calculator"),
             html.P("""\An easy to use cost calculator for starting and maintaining a Design to Data (D2d) enzyme course.""")
            ],
            md=4,),
         dbc.Col(
             [html.H2("Cost Graph"),
              dcc.Graph(
                  figure={
                      "data": [
                          {"x": [1, 2, 3], 
                           "y": [1, 4, 9]}
                      ]
                  }),
             ]),])],
    className="mt-4",)

def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout

def open_browser():
    webbrowser.open_new("http://localhost:{}".format(port))
    
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()
port = 8050     
application = app.server

if __name__ == '__main__':
    Timer(0, open_browser).start();
    app.run_server(debug=True, port=port)