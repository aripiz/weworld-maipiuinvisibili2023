from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

import json
from pathlib import Path
import plotly.express as px
import pandas as pd

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP]) #

path = Path("/Users/ariele/Library/CloudStorage/GoogleDrive-ariele.piziali@gmail.com/Il mio Drive/Lavoro/WeWorld/Italiano/2023/Notebooks/app/")

app.layout = html.Div([
    html.H4("WeWorld Mai più invisibili 2023: evoluzione dell'indice"),
    html.P("Seleziona il sottoindice:"),
    dcc.Dropdown(
        id='subindex', 
        options=["Totale", "Contesto", "Bambini", 'Donne'],
        value="Totale",
        style={"width": "50%"}
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("subindex", "value"))
def display_choropleth(subindex):
    df = pd.read_pickle(path /"indice_territori_mappe.pickle")
    with open(path/'italy_regions_low.json', "r") as geo_file: geogejson_territori = json.load(geo_file)

    fig = px.choropleth(df, geojson=geogejson_territori, locations='codice_istat',
                    featureidkey="properties.istat_code_num", projection='natural earth', animation_frame='anno',
                    title="WeWorld <i>Mai più invisibili 2023</i>: evoluzione dell'indice",
                    color=subindex,
                    range_color=[20,80],
                    color_continuous_scale='RdYlGn',
                    hover_name='territorio',
                    hover_data={'codice_istat':False, 'anno': False, 
                                'Totale': ':.3g', 'Contesto':':.3g', 'Bambini':':.3g', 'Donne':':.3g'},
                    ) 
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig


app.run_server(debug=True)
