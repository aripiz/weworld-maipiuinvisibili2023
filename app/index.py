# index.py

from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

# Title
TITLE = 'WeWorld Mai più invisibili 2023'

# Themes and colors
THEME = dbc.themes.LUMEN
FIGURE_TEMPLATE = 'lumen'
STYLE_CSS = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/app/assets/bootstrap.min.csss"
DBC_CSS = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

#COLOR_SCALE_OLD = ['#00876c','#65a971','#f9e68f','#f4b164', '#ea7a50','#d43d51'][::-1]
COLOR_SCALE = ["#D53A50", "#E97B4E", "#F0B060", "#DECE58", "#64A972", "#3E876B"]

# Mapbox
MAP_TOKEN = "pk.eyJ1IjoiYXJpcGl6IiwiYSI6ImNsZjE5YzJrbjA2OWMzcHM0YzJyaXIydHAifQ.SWcexWOHS6ddnrGBx7idAw"
MAP_STYLE = "mapbox://styles/aripiz/clf1ay30l004n01lnzi17hjvj"

# Files link
DATA_FILE ="https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/maipiuinvisibili2023_data.csv"
META_FILE = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/maipiuinvisibili2023_metadata.csv"
GEO_FILE = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/italy_regions_low.json"

NOTES_FILE = "https://github.com/aripiz/weworld-maipiuinvisibili2023/raw/master/data/WeWorld-MaiPi%C3%B9Invisibili-2023_NoteTecniche.pdf"

REPORT_FILE = ""

# Loading
df_data = pd.read_csv(DATA_FILE)
df_meta = pd.read_csv(META_FILE, index_col=0)

# App 
app = Dash(
    __name__, 
    title=TITLE,
    external_stylesheets=[THEME, DBC_CSS], 
    suppress_callback_exceptions=True, 
    use_pages=True,
    #meta_tags=[{"name": "viewport", "content": "width=device-width"}]
    )