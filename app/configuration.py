# Title
TITLE = 'Mai più invisibili 2023'

# Themes and colors
FIGURE_TEMPLATE = 'zephyr'
DBC_CSS = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
COLOR_SCALE = ["#D53A50", "#E97B4E", "#F0B060", "#DECE58", "#64A972", "#3E876B"]

# Mapbox 
import os
MAP_TOKEN = os.getenv("MAP_TOKEN")
# MAP_TOKEN = "pk.eyJ1IjoiYXJpcGl6IiwiYSI6ImNsZjE5YzJrbjA2OWMzcHM0YzJyaXIydHAifQ.SWcexWOHS6ddnrGBx7idAw" # Only usable from weworld-maipiuinvisibili.onrender.com
if MAP_TOKEN is not None: MAP_STYLE = "mapbox://styles/aripiz/clf1ay30l004n01lnzi17hjvj"
else: MAP_STYLE = "carto-positron"

# Files link
DATA_FILE = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/maipiuinvisibili2023_data.csv"
META_FILE = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/maipiuinvisibili2023_metadata.csv"
GEO_FILE = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/italy_regions_low.json"
NOTES_FILE = "https://github.com/aripiz/weworld-maipiuinvisibili2023/raw/master/data/WeWorld-MaiPi%C3%B9Invisibili-2023_NoteTecniche.pdf"
REPORT_FILE = "https://github.com/aripiz/weworld-maipiuinvisibili2023/raw/master/data/WeWorld-MaiPi%C3%B9Invisibili-2023_Rapporto.pdf"