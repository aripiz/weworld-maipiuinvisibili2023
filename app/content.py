# content.py

from index import app
from dash import dcc, html, page_container
import dash_bootstrap_components as dbc

from layout.callbacks  import render_data
from layout.callbacks import render_tab
from layout.callbacks import toggle_modal
from layout.callbacks import toggle_collapse

from configuration import NOTES_FILE, REPORT_FILE

from layout.layout_download import modal_data_download

# Header and footer
header = dbc.Row(
            dbc.Col(dcc.Markdown("# WeWorld _Mai più invisibili 2023_"), style={'text-align':'center'})
)

footer = dbc.Navbar([
    html.Div("WeWorld"), #html.Img(src="assets/logo_weworld.png", height='15px'),#
    html.Div(["created by ", html.A("aripiz", href="https://github.com/aripiz", className='link-warning')])],
    style={"display": "flex", 'justify-content': 'space-between', 'padding-left':'4rem', 'padding-right':'4rem', 'flex':'1', },
    #color="primary",
    fixed='bottom',
                #"padding-top": "1rem", "padding-bottom": "1rem"
)      
            #style={"position": "absolute", "bottom": "0", 'left':"0", "right":"0", "width": "100%", "height": "2.5rem","text-align":"center"}

footer_old = dbc.Row([
    dbc.Col(html.Div("WeWorld Onlus"), style={'text-align':'left'} ),
    dbc.Col(html.Div(["created by ", html.A("aripiz", href="https://github.com/aripiz", className='link-warning')]), style={'text-align':'right'})],   
    justify='around',
    class_name='fixed-bottom',
    style={'background-color': '#005D9E', 'color':'white', "margin-top":"auto", 'padding-left':'1.5rem', 'padding-right':'1.5rem' }
                #"padding-top": "1rem", "padding-bottom": "1rem"
)      
            #style={"position": "absolute", "bottom": "0", 'left':"0", "right":"0", "width": "100%", "height": "2.5rem","text-align":"center"}

# Sections
pages_nav = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Panoramica", active='exact', href='/')),
        dbc.NavItem(dbc.NavLink("Esplora i dati", active='exact', href="/data")),
        dbc.NavItem(dbc.NavLink("Metodologia", active='exact', href="/methodology")),
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("Rapporto", href=REPORT_FILE), 
                dbc.DropdownMenuItem("Note tecniche", href=NOTES_FILE), 
                dbc.DropdownMenuItem("Dati", id='open_download', n_clicks=0),
                modal_data_download
            ],
            label="Download",
            in_navbar=True,
        ),
    ],
    brand= [html.Img(src="assets/logo_weworld.png", height='30px'), html.Img(src="assets/logo_maipiuinvisibili2023_neg.png", height="30px")], # TITLE,
    brand_href="https://www.weworld.it",
    fixed='top',
    color='primary',
    dark=True
)

page = dbc.Row(dbc.Col(page_container), style={ 'padding-top': '80px', 'padding-bottom': '60px'}) #"display": "flex", "flex-direction": "column",'justify-content': 'around',

# Main layout
app.layout = dbc.Container(
    [
        #header,
        pages_nav,
        page,
        footer
    ],
    #fluid=True,
    className="dbc",     
    #style={"padding": "1.5rem"}
    #style = {"display": "flex","flex-direction": "column","height": "100vh"}
)
