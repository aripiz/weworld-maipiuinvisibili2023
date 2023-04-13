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
                    html.P("Seleziona una componente:"),
                    dcc.Dropdown(
                    id = 'feature',
                    options = features_list,
                    value = features_list[0],
                    style = {"width": "60%"})
                ]),
                dbc.Col([
                    html.P("Seleziona un anno:"),
                    dcc.Slider(
                        years_list[0],
                        years_list[-1],
                        step = None,
                        id ='slider_year',
                        value = years_list[-1],
                        marks = {str(year): str(year) for year in years_list})],
                    width=3)],
                justify='evenly'),
                dcc.Graph(
                    id = "map",
                    #style = {'height': '100%'},
                    responsive = True
                )
            ])

tab_map_indicators = html.Div([
                dbc.Row([
                dbc.Col([
                    html.P("Seleziona un indicatore:"),
                    dcc.Dropdown(
                    id='indicator',
                    options=indicators_list,
                    value=indicators_list[0],
                    style={"width": "100%"})]
                ),
                dbc.Col([
                    html.P("Scegli la tipologia:"),
                    dbc.RadioItems(
                    id='indicator_kind',
                    options=kind_list,
                    inline=True,
                    value= kind_list[1])],
                    width=2
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
                    width=3
                )], justify='evenly'),
                dcc.Graph(
                    id="indicators_map",
                    #style={'height': '100%'},
                    responsive=True
                )
            ])

tab_correlations = html.Div([
                dbc.Row([
                dbc.Col([
                    html.P("Seleziona una componente:"),
                    dcc.Dropdown(
                    id="dimension_x",
                    options = features_list,
                    value=features_list[0],
                    style={"width": "75%"}
                )]),
                dbc.Col([
                    html.P("Seleziona un'altra componente:"),
                    dcc.Dropdown(
                    id="dimension_y",
                    options = features_list,
                    value=features_list[1],
                    style={"width": "75%"}
                )]),
                dbc.Col([
                    html.P("Seleziona un anno:"),
                    dcc.Slider(
                        years_list[0],
                        years_list[-1],
                        step=None,
                        id='slider_year',
                        value=years_list[-1],
                        marks={str(year): str(year) for year in years_list})],
                    width=3)],
                justify='evenly'),
                dcc.Graph(
                    id="dimensions_correlation",
                    #style={'height': '100%'},
                    responsive=True
                ),
            ])

tab_ranking = html.Div([
                dbc.Row([
                dbc.Col([
                html.P("Seleziona una componente:"),
                dcc.Dropdown(
                    id="ranking_feature",
                    options = features_list,
                    value=features_list[0],
                    style={"width": "75%"}
                )]),
                dbc.Col([
                html.P("Seleziona un anno:"),
                dcc.Slider(
                        years_list[0],
                        years_list[-1],
                        step=None,
                        id='slider_year',
                        value=years_list[-1],
                        marks={str(year): str(year) for year in years_list})
                ],width=3)
                ]),
                html.Div(
                    id='ranking_table',
                    style={"height": "55vh", "overflow": "scroll"},
                )
            ])

tab_evolution = html.Div([
                dbc.Row([
                dbc.Col([
                html.P("Seleziona le componenti:"),
                dcc.Dropdown(
                    id="evolution_feature",
                    options = features_list,
                    value=features_list[0],
                    style={"width": "75%"},
                    multi=True
                )]),
                dbc.Col([
                html.P("Seleziona i territori:"),
                dcc.Dropdown(
                    id='evolution_territory',
                    options = territories_list ,
                    value = 'Italia',
                    style={"width": "75%"},
                    multi=True
                )])]),
                dcc.Graph(
                    id="evolution_plot",
                    #style={'height': '100%'},
                    responsive=True
                )
            ])

tab_radar = html.Div([
                dbc.Row([
                dbc.Col([
                html.P("Seleziona i territori:"),
                dcc.Dropdown(
                    id='radar_territory',
                    options = territories_list ,
                    value = 'Italia',
                    style={"width": "75%"},
                    multi=True
                )]),
                dbc.Col([
                html.P("Seleziona gli anni:"),
                dcc.Dropdown(
                    id='radar_year',
                    options = years_list ,
                    value = [years_list[0],years_list[-1]],
                    #style={"width": "75%"},
                    multi=True
                )],width=3)
                ]),
                dbc.Row([
                dbc.Col(html.Div(
                    id='radar_table',
                    style={"height": "55vh", "overflow": "scroll"},
                )),
                dbc.Col(dcc.Graph(
                    id="radar_chart",
                    #style={'height': '100%'},
                    responsive=True
                ))
                ])
                
            ])

