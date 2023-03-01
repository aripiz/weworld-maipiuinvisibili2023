# app.py
# Dash webapp to present WeWorld "Mai più invisibili 2023" index and indicators
# available at http://aripiz.pythonanywhere.com/

from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import plotly.express as px
import pandas as pd
import plotly.io as pio

# Title
title = 'WeWorld Mai più invisibili 2023'

# Themes
figure_template = 'cosmo'
theme = dbc.themes.COSMO
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

load_figure_template(figure_template)
pio.templates.default = figure_template


app = Dash(__name__, external_stylesheets=[theme, dbc_css], suppress_callback_exceptions=True, title=title)

# Files link
index_data_file = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/sottoindici_territori.csv"
indicators_meta_file = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/metadati_indicatori_territori.csv"
indicators_data_file = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/indicatori_dati_territori.csv"
dimensions_data_file = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/dimensioni_territori.csv"
geo_data_file = "https://raw.githubusercontent.com/aripiz/weworld-maipiuinvisibili2023/master/data/italy_regions_low.json"

# Data loading
index_data = pd.read_csv(index_data_file)
indicators_data = pd.read_csv(indicators_data_file)
dimensions_data = pd.read_csv(dimensions_data_file)
indicators_meta = pd.read_csv(indicators_meta_file, index_col=0)
#geo_data = pd.read_json(geo_data_file,lines=True).to_dict('records')[0]


app.layout = dbc.Container([
        dcc.Store(id="store"),
        dcc.Markdown("# WeWorld _Mai più invisibili 2023_"),
        #html.H1(children="WeWorld Mai più invisibili 2023", style={"text-align": "center", }),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(label="Mappa indice", tab_id="index"),
                dbc.Tab(label="Mappa dimensioni", tab_id="dimensions"),
                dbc.Tab(label="Mappa indicatori", tab_id="indicators"),
                dbc.Tab(label="Correlazione dimensioni", tab_id="correlations"),
                dbc.Tab(label="Classifica", tab_id="ranking"),
                dbc.Tab(label="Evoluzione temporale", tab_id="evolution"),
            ],
            id="tabs",
            active_tab="index",
        ),
        html.Div(id="tab-content", className="p-4"),
    ],
    fluid=True,
    className="dbc"
)

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")])
def render_tab_content(active_tab, data):
    if active_tab is not None:
        if active_tab == "index":
            options_list = index_data.columns[2:-2]
            return html.Div([
                html.P("Seleziona un indice:"),
                dcc.Dropdown(
                    id='subindex',
                    options=options_list,
                    value=options_list[-1],
                    style={"width": "40%"}
                ),
                dcc.Graph(
                    id="index_map",
                    style={'width': '90vw', 'height': '70vh'}
                )
            ])
        elif active_tab == "indicators":
            #return "Sezione ancora da creare."
            options_list = [f"{num}: {indicators_meta.loc[num]['nome']}" for num in indicators_meta.index]
            return html.Div([
                html.P("Seleziona un indicatore:"),
                dcc.Dropdown(
                    id='indicator',
                    options = options_list ,
                    value=options_list[0],
                    style={"width": "80%"}
                ),
                dcc.Graph(
                    id="indicators_map",
                    style={'width': '90vw', 'height': '70vh'}
                    #responsive=True
                )
            ])
        elif active_tab == "correlations":
            options_list = dimensions_data.columns[2:-2]
            return html.Div([
                html.P("Seleziona due dimensioni da confrontare:"),
                dbc.Row([
                dbc.Col(dcc.Dropdown(
                    id="dimension_x",
                    options = options_list,
                    value=options_list[0],
                    style={"width": "75%"}
                )),
                dbc.Col(dcc.Dropdown(
                    id='dimension_y',
                    options = options_list ,
                    value = options_list[1],
                    style={"width": "75%"}
                ))]),
                dcc.Graph(
                    id="dimensions_correlation",
                    style={'width': '90vw', 'height': '70vh'}
                    #responsive=True
                ),
            ])
        elif active_tab == "dimensions":
            options_list = dimensions_data.columns[2:-2]
            return html.Div([
                html.P("Seleziona una dimensione:"),
                dcc.Dropdown(
                    id='dimension',
                    options = options_list ,
                    value=options_list[0],
                    style={"width": "80%"}
                ),
                dcc.Graph(
                    id="dimensions_map",
                    style={'width': '90vw', 'height': '70vh'}
                    #responsive=True
                )
            ])
        elif active_tab == 'ranking':
            options_list = dimensions_data.columns[2:-2]
            years_list = index_data['anno'].unique() 
            return html.Div([
                dbc.Row([
                dbc.Col([
                html.P("Seleziona un sottoindice o una dimensione:"),
                dcc.Dropdown(
                    id="feature",
                    options = options_list,
                    value=options_list[0],
                    style={"width": "75%"}
                )]),
                dbc.Col([
                html.P("Seleziona un anno:"),
                dcc.Dropdown(
                    id='year',
                    options = years_list ,
                    value = years_list[-1],
                    style={"width": "75%"}
                )])]),
            ])
    return "Nessun elemento selezionato."

@app.callback(
    Output("index_map", "figure"),
    Input("subindex", "value"))
def display_map_index(subindex):
    fig = px.choropleth(index_data, geojson=geo_data_file,
        locations='codice_istat', featureidkey="properties.istat_code_num",
        projection='natural earth', animation_frame='anno',
        color=subindex,
        range_color=[20,80],
        color_continuous_scale='RdYlGn',
        hover_name='territorio',
        hover_data={'codice_istat':False, 'anno': False,
                    'Generale': ':.3g', 'Contesto':':.3g', 'Bambini':':.3g', 'Donne':':.3g'},
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
        coloraxis_colorbar=dict(title="Punteggio"),
        sliders = [dict(len=0.25, active= 4, x=0.5,xanchor='center', currentvalue= {"prefix": "Anno: "})],
    )
    fig["layout"].pop("updatemenus")
    return fig

@app.callback(
    Output("indicators_map", "figure"),
    Input("indicator", "value"))
def display_map_indicators(indicator):
    indicator = indicator.split(":")[0]
    if indicators_meta.loc[int(indicator)]['inverted']=='yes':
        color_scale = 'RdYlGn_r'
        limits_scale = [indicators_meta.loc[int(indicator)]['best_value'], indicators_meta.loc[int(indicator)]['worst_value']]
    else:
        color_scale = 'RdYlGn'
        limits_scale = [indicators_meta.loc[int(indicator)]['worst_value'], indicators_meta.loc[int(indicator)]['best_value']]
    fig = px.choropleth(indicators_data, geojson=geo_data_file,
        locations='codice_istat', featureidkey="properties.istat_code_num",
        projection='natural earth', animation_frame='anno',
        color=indicator,
        range_color=limits_scale,
        color_continuous_scale=color_scale,
        hover_name='territorio',
        hover_data={'codice_istat':False, 'anno': False,
                    indicator: ':.3g'},
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
        coloraxis_colorbar=dict(title=indicators_meta.loc[int(indicator)]['unità']),
        sliders = [dict(len=0.25, active= 4, x=0.5,xanchor='center', currentvalue= {"prefix": "Anno: "})]
    )
    fig["layout"].pop("updatemenus")
    return fig

@app.callback(
    Output("dimensions_map", "figure"),
    Input("dimension", "value"))
def display_map_dimensions(dimension):
    fig = px.choropleth(dimensions_data, geojson=geo_data_file,
        locations='codice_istat', featureidkey="properties.istat_code_num",
        projection='natural earth', animation_frame='anno',
        color=dimension,
        range_color=[0,100],
        color_continuous_scale='RdYlGn',
        hover_name='territorio',
        hover_data={'codice_istat':False, 'anno': False,
                    dimension: ':.3g'},
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
        coloraxis_colorbar=dict(title='Punteggio'),
        sliders = [dict(len=0.25, active= 4, x=0.5,xanchor='center', currentvalue= {"prefix": "Anno: "})]
    )
    fig["layout"].pop("updatemenus")
    return fig

@app.callback(
    Output("dimensions_correlation", "figure"),
    Input('dimension_x', 'value'),
    Input('dimension_y', 'value'))
def display_corr_dimensions(dimension_x, dimension_y):
    fig = px.scatter(dimensions_data, x=dimension_x, y=dimension_y, 
                 hover_name='territorio', color='area', animation_frame='anno',
                 hover_data={'area':False, 'anno': False, dimension_x: ':.3g', dimension_y:':.3g'},)
    fig.update_traces(marker={'size': 15})
    fig.update_layout(
        legend_title = 'Area',
        sliders = [dict(len=0.25, active= 4, x=0.5,xanchor='center', currentvalue= {"prefix": "Anno: "})]
    )
    fig["layout"].pop("updatemenus")
    return fig
'''
@app.callback(
    Output("ranking_table", "figure"),
    Input("feature", "value"))
def display_ranking(feature):

    return "In preparazione"
'''

if __name__ == "__main__":
    app.run(debug=True)
