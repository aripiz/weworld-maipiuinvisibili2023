# tabs.py

from index import df_data, df_meta
from dash import dcc, html
import dash_bootstrap_components as dbc

# Options
features_list = df_data.columns[4:23]
years_list = df_data['anno'].unique()
indicators_list = [f"{num}: {df_meta.loc[num]['nome']}" for num in df_meta.index]
kind_list = ['Dati', 'Punteggi']
territories_list = df_data['territorio'].unique()

# Tabs
tab_map_features = html.Div([
                dbc.Row([
                dbc.Col([
                    dbc.Label("Seleziona una componente:"),
                    dcc.Dropdown(
                    id = 'feature',
                    options = features_list,
                    value = features_list[0],
                    #style = {"width": "80%"}
                )], lg = 6, xs = 12),
                dbc.Col([
                    dbc.Label("Seleziona un anno:"),
                    dcc.Slider(
                        years_list[0],
                        years_list[-1],
                        step = None,
                        id ='slider_year',
                        value = years_list[-1],
                        marks = {str(year): str(year) for year in years_list},
                        )
                ], lg = 3, xs =12)],
                justify='around'),
                dbc.Row(dbc.Col(
                dcc.Graph(
                    id = "map",
                    #style = {'height': '100%'},
                    responsive = True
                )), justify = 'around', class_name = 'mt-2')
            ])

tab_map_indicators = html.Div([
                dbc.Row([
                dbc.Col([
                    dbc.Label("Seleziona un indicatore:"),
                    dcc.Dropdown(
                    id='indicator',
                    options=indicators_list,
                    value=indicators_list[0],
                    style={"width": "100%"})],
                    lg = 6, xs = 12
                ),
                dbc.Col([
                    dbc.Label("Scegli la tipologia:"),
                    dbc.RadioItems(
                    id='indicator_kind',
                    options=kind_list,
                    inline=True,
                    value= kind_list[1])],
                    lg = 3, xs = 12
                ),
                dbc.Col([
                    html.P("Seleziona un anno:"),
                    dcc.Slider(
                        years_list[0],
                        years_list[-1],
                        step=None,
                        id='slider_year',
                        value=years_list[-1],
                        marks={str(year): str(year) for year in years_list})],
                    lg = 3, xs = 12
                )], justify='around'),
                dbc.Row(dbc.Col(
                dcc.Graph(
                    id="indicators_map",
                    #style={'height': '100%'},
                    responsive=True
                )), justify = 'around', class_name = 'mt-2')
            ])

tab_correlations = html.Div([
                dbc.Row([
                dbc.Col([
                    dbc.Label("Seleziona una componente:"),
                    dcc.Dropdown(
                    id="dimension_x",
                    options = features_list,
                    value=features_list[0],
                    #style={"width": "75%"}
                )], lg = 4, xs =12),
                dbc.Col([
                    dbc.Label("Seleziona un'altra componente:"),
                    dcc.Dropdown(
                    id="dimension_y",
                    options = features_list,
                    value=features_list[1],
                    #style={"width": "75%"}
                )], lg = 4, xs =12),
                dbc.Col([
                    dbc.Label("Seleziona un anno:"),
                    dcc.Slider(
                        years_list[0],
                        years_list[-1],
                        step=None,
                        id='slider_year',
                        value=years_list[-1],
                        marks={str(year): str(year) for year in years_list})
                    ], lg = 3, xs =12)],
                justify='around'),
                dbc.Row(dbc.Col(dcc.Graph(
                    id="dimensions_correlation",
                    #style={'height': '100%'},
                    responsive=True
                )), justify = 'around', class_name = 'mt-2'),
            ])

tab_ranking = html.Div([
                dbc.Row([
                dbc.Col([
                dbc.Label("Seleziona una componente:"),
                dcc.Dropdown(
                    id="ranking_feature",
                    options = features_list,
                    value=features_list[0],
                    #style={"width": "75%"}
                )], lg = 6, xs =12),
                dbc.Col([
                dbc.Label("Seleziona un anno:"),
                dcc.Slider(
                        years_list[0],
                        years_list[-1],
                        step=None,
                        id='slider_year',
                        value=years_list[-1],
                        marks={str(year): str(year) for year in years_list})
                ], lg = 3, xs =12)
                ], justify='around'),
                dbc.Row(dbc.Col(html.Div(
                    id='ranking_table',
                    style={"height": "60vh", "overflow": "scroll"},
                )), justify = 'around', class_name = 'mt-2')
            ])

tab_evolution = html.Div([
                dbc.Row([
                dbc.Col([
                dbc.Label("Seleziona le componenti:"),
                dcc.Dropdown(
                    id="evolution_feature",
                    options = features_list,
                    value=features_list[0],
                    #style={"width": "75%"},
                    multi=True
                )], lg = 6, xs =12),
                dbc.Col([
                dbc.Label("Seleziona i territori:"),
                dcc.Dropdown(
                    id='evolution_territory',
                    options = territories_list ,
                    value = 'Italia',
                    #style={"width": "75%"},
                    multi=True
                )], lg = 6, xs =12)
                ], justify = 'around'),
                dbc.Row(dbc.Col(
                dcc.Graph(
                    id="evolution_plot",
                    #style={'height': '100%'},
                    responsive=True
                )), justify = 'around', class_name = 'mt-2')
            ])

tab_radar = html.Div([
                dbc.Row([
                dbc.Col([
                dbc.Label("Seleziona i territori:"),
                dcc.Dropdown(
                    id='radar_territory',
                    options = territories_list ,
                    value = 'Italia',
                    #style={"width": "75%"},
                    multi=True
                )], lg = 6, xs =12),
                dbc.Col([
                dbc.Label("Seleziona gli anni:"),
                dcc.Dropdown(
                    id='radar_year',
                    options = years_list ,
                    value = [years_list[0],years_list[-1]],
                    #style={"width": "75%"},
                    multi=True
                )], lg = 3, xs =12)
                ], justify = 'around'),
                dbc.Row([
                dbc.Col(html.Div(
                    id='radar_table',
                    style={"height": "60vh", "overflow": "scroll"},
                ), lg = 6, xs =12),
                dbc.Col(dcc.Graph(
                    id="radar_chart",
                    #style={'height': '100%'},
                    responsive=True
                ), lg = 6, xs =12)
                ], justify = 'around', class_name = 'mt-2')
            ])

