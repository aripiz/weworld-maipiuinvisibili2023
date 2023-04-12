# methodology.py

from dash import html, register_page
import dash_bootstrap_components as dbc
from index import TITLE

register_page(__name__, name = TITLE )


layout = html.Div(
    [
        html.H3('Titolo'),
        html.P('Prova.'),
    ],
)