# index.py

from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

from configuration import DATA_FILE, META_FILE, TITLE, DBC_CSS

# Loading
df_data = pd.read_csv(DATA_FILE)
df_meta = pd.read_csv(META_FILE, index_col=0)

# App 
app = Dash(
    __name__, 
    title=TITLE,
    external_stylesheets=[DBC_CSS], 
    suppress_callback_exceptions=True, 
    use_pages=True,
    )