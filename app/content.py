# content.py

from index import app
from dash import dcc, html, page_container
import dash_bootstrap_components as dbc

from layout.callbacks import render_data
from layout.callbacks import render_tab
from layout.callbacks import toggle_modal

from index import NOTES_FILE, REPORT_FILE

from layout.data_download import modal_data_download

# Header and footer
header = dbc.Row(
            dbc.Col(dcc.Markdown("# WeWorld _Mai più invisibili 2023_"), style={'text-align':'center'})
)

footer = dbc.Row([
                dbc.Col(html.Div("WeWorld Onlus"), style={'text-align':'left'} ),
                dbc.Col(html.Div(["created by ", html.A("aripiz", href="https://github.com/aripiz")]), style={'text-align':'right'} ),
                ],   
                justify='end',
                style={ "margin-top":"auto", } #"padding-top": "1rem", "padding-bottom": "1rem"
)      
            #style={"position": "absolute", "bottom": "0", 'left':"0", "right":"0", "width": "100%", "height": "2.5rem","text-align":"center"}

# Sections
pages_nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Panoramica", active='exact', href='/')),
        dbc.NavItem(dbc.NavLink("Esplora i dati", active='exact', href="/data")),
        dbc.NavItem(dbc.NavLink("Metodologia e definizioni", active='exact', href="/methodology")),
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("Rapporto", href="#"), 
                dbc.DropdownMenuItem("Note tecniche", href=NOTES_FILE), 
                dbc.DropdownMenuItem("Dati", id='open_download', n_clicks=0),
                modal_data_download
            ],
            label="Download",
            nav=True,
        ),
    ],
    pills=True, 
    horizontal='center'
)

page = dbc.Row(dbc.Col(page_container), className="my-2", style={"display": "flex", "flex-direction": "column",'justify-content': 'around'})

# Main layout
app.layout = dbc.Container(
    [
        #header,
        pages_nav,
        page,
        #footer
    ],
    #fluid=True,
    className="dbc p-4",     
    #style = {"display": "flex","flex-direction": "column","height": "100vh"}
)
