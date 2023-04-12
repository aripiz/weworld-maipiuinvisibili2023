# index.py

from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

# Title
TITLE = 'WeWorld Mai più invisibili 2023'

# Themes
THEME = dbc.themes.COSMO
FIGURE_TEMPLATE = 'cosmo'
DBC_CSS = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
COLOR_SCALE = ['#00876c','#65a971','#f9e68f','#f4b164', '#ea7a50','#d43d51'][::-1]

# Mapbox
MAP_TOKEN = "pk.eyJ1IjoiYXJpcGl6IiwiYSI6ImNsZjE5YzJrbjA2OWMzcHM0YzJyaXIydHAifQ.SWcexWOHS6ddnrGBx7idAw"
MAP_STYLE = "mapbox://styles/aripiz/clf1ay30l004n01lnzi17hjvj"

# Files link
DATA_FILE ="https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/maipiuinvisibili2023_data.csv"
META_FILE = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/maipiuinvisibili2023_metadata.csv"
GEO_FILE = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/italy_regions_low.json"

# Loading
df_data = pd.read_csv(DATA_FILE)
df_meta = pd.read_csv(META_FILE, index_col=0)

# App 
app = Dash(
    __name__, 
    title=TITLE,
    external_stylesheets=[THEME,DBC_CSS], 
    suppress_callback_exceptions=True, 
    use_pages=True,
    #meta_tags=[{"name": "viewport", "content": "width=device-width"}]
    )