import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
#             dbc.NavItem(
#                 dbc.NavLink("Time-Series", 
#                             href="/time-series")),
            dbc.DropdownMenu(nav=True,
                             in_navbar=True,
                             label="Menu",
                             children=[
                                 dbc.DropdownMenuItem("Reagents and Consumables", id="consumables", href="consumables"),
                                 dbc.DropdownMenuItem("Equipment", id="equipment", href="equipment"),
                                 dbc.DropdownMenuItem("Common Reagents", id="reagents", href="reagents"),
                                 dbc.DropdownMenuItem(divider=True),
                                 dbc.DropdownMenuItem("D2D Information", id="info", href="info"),
                             ],
                            ),
        ],
        brand="Home",
        brand_href="/home",
        sticky="top")
    return navbar