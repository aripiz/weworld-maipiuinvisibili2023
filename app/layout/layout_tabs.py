# tabs.py

from index import df_data, df_meta
from dash import dcc, html
import dash_bootstrap_components as dbc

from index import NOTES_FILE

# Options
features_list = df_data.columns[4:23]
years_list = df_data['anno'].unique()
indicators_list = [f"{num}: {df_meta.loc[num]['nome']}" for num in df_meta.index]
kind_list = ['Dati', 'Punteggi']
territories_list = df_data['territorio'].unique()

# Data tabs
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

# Methodology tabs
tab_indicators= html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Label("Seleziona un indicatore:"),
            dcc.Dropdown(
                id='indicator',
                options=indicators_list,
                value=indicators_list[0],
                style={"width": "100%"}),
        ]),
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Indicatore", className="card-title"),
                html.H5(id="indicator_num", className="card-text")
            ])),
            lg = 2, xs = 4,
        ),
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Nome", className="card-title"),
                html.Div(id="indicator_name", className="card-text")
            ])),
            lg=6, xs=8,
        ),
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Sottoindice", className="card-title"),
                html.Div(id="indicator_sub", className="card-text")
            ])),
            lg=2, xs=6,
        ),
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Dimensione", className="card-title"),
                html.Div(id="indicator_dim", className="card-text")
            ])),
            lg=2, xs=6,
        ),
    ], class_name = 'mt-2'),
    dbc.Row([
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Descrizione", className="card-title"),
                html.Div(id="indicator_des", className="card-text")
            ])),
            lg=10, xs=12,
        ),
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Unità di misura", className="card-title"),
                html.Div(id="indicator_unit", className="card-text")
            ])),
            lg=2, xs=12,
        ),
    ], class_name = 'mt-2'),
    dbc.Row([
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Aggiornamento", className="card-title"),
                html.Div(id="indicator_update", className="card-text")
            ])),
            lg = 3, xs = 12,
        ),
        dbc.Col(
            dbc.Card(dbc.CardBody([
                html.H4("Fonte", className="card-title"),
                html.A(id="indicator_source", className="card-text", target="_blank", rel="noopener noreferrer")
            ])),
            lg=9, xs=12,
        ),
        # dbc.Col(
        #     dbc.Card(dbc.CardBody([
        #         html.H4("Link", className="card-title"),
        #         html.A("Dati originali", , className="card-text")
        #     ])),
        #     lg=3, xs=6,
        # ),
    ], class_name = 'mt-2'),
])

tab_construction = html.Div([
    dbc.Row(
        dbc.Col([
            dcc.Markdown(
                """
                L’Indice è stato costruito seguendo un processo in cinque fasi (raccolta dati, imputazione valori mancanti, trasformazione indicatori, normalizzazione indicatori, aggregazione) che, a partire dai dati originali permette di ottenere e confrontare i punteggi di ciascuna componente (Indicatori, Dimensioni, Sottoindici, Indice generale) negli anni dal 2018 al 2022 per ciascun territorio (Regione/Provincia Autonoma, Area o Italia). 
                """),
                html.Div(["Una descrizione dettagliata del metodo seguito è disponibile nelle ", html.A("Note tecniche.", href=NOTES_FILE)]),
                html.Br()
            ])
    ),
    dbc.Row([
        dbc.Col([
            dcc.Markdown("### La struttura"),
            dcc.Markdown(
                """
                La necessità di valutare separatamente le performance dei territori in relazioni ai tre sottoindici nasce da un assunto ben preciso: **intervenire per garantire inclusione tout court, senza tenere conto degli specifici bisogni e rischi di genere e generazionali,** adottando dunque un approccio intersezionale, non consente una piena realizzazione dei diritti e delle capacitazioni di donne, bambini e adolescenti. 
                
                Una reale inclusione di queste categorie, infatti, può compiersi solo attraverso la **creazione, implementazione e il monitoraggio di policy** adeguate che devono essere al tempo stesso **multidimensionali,** per tenere conto dell’intreccio esistente tra i diritti di donne e minori, e **targettizzate,** ovvero tarate sulle loro necessità specifiche. **Per questo è necessario guardare ancora più da vicino alle loro condizioni.** 
                
                L’Italia offre un contesto tendenzialmente favorevole all’inclusione delle categorie più vulnerabili, eppure queste continuano a vivere in condizioni di svantaggio e fragilità. 
                I valori ottenuti dalle regioni nei tre sottoindici sono in certi casi molto diversi, al punto da apparire quasi discordanti. 
                
                È necessario quindi procedere su due fronti paralleli e complementari: da una parte è fondamentale **lavorare sui contesti** in cui donne, bambini e adolescenti vivono e renderli il più favorevoli possibile al loro pieno sviluppo; dall’altra non si può di certo pensare che contesti favorevoli siano di per sé sufficienti a soddisfare i bisogni e le istanze di donne, bambini e adolescenti per i quali sono necessarie **politiche adeguate e interventi mirati.**
                """
            ),
        ], lg=6, xs =12),
        dbc.Col(
            dbc.CardGroup([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Contesto", className="card-title"),
                        dbc.ListGroup([ dbc.ListGroupItem(dim) for dim in df_meta.loc[[1,3,5,7,9],'dimensione']],
                        numbered=False, flush=True,
                        className="card-text",)
                        ])
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Bambini", className="card-title"),
                        dbc.ListGroup([ dbc.ListGroupItem(dim) for dim in df_meta.loc[[11,13,15,17,19],'dimensione']],
                        numbered=False, flush=True,
                        className="card-text",)
                        ])
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Donne", className="card-title"),
                        dbc.ListGroup([ dbc.ListGroupItem(dim) for dim in df_meta.loc[[21,23,25,27,29],'dimensione']],
                        numbered=False, flush=True,
                        className="card-text",)
                    ])
                )
            ]),
        align='center', lg= 6, xs =12)
    ], justify="around"),
    dbc.Row([
        dbc.Col([
            dcc.Markdown("### L'aggregazione"),
            dcc.Markdown("""
                L’Indice di ogni territorio consiste in un **punteggio 0-100** elaborato aggregando i dati normalizzati dei suoi 30 Indicatori in **tre diverse fasi**. 
                
                Innanzitutto sono calcolati i punteggi di ciascuna delle **Dimensioni** prendendo la media aritmetica dei punteggi dei due Indicatori che la compongono.
                Successivamente, per evitare una piena compensabilità fra le Dimensioni, il punteggio dei **Sottoindici** è determinato dalla media geometrica delle Dimensioni che ne fanno parte. La media geometrica è infine utilizzata anche per calcolare l’**Indice generale** a partire dai 3 Sottoindici. 
                
                Con un’aggregazione di questo tipo, una pessima prestazione in **un aspetto giudicato fondamentale per l’inclusione non può venire del tutto o in parte compensato da un punteggio elevato in altre.** 
                """)
        ], lg=6, xs =12),
        dbc.Col(
            dbc.CardGroup([
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Dimensioni", className="card-title"),
                        dcc.Markdown("Il punteggio delle 15 Dimensioni è ottenuto dalla **media aritmetica** dei punteggi dei **2 Indicatori** che compongono ciascuna.", className="card-text")
                        ])
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Sottoindici", className="card-title"),
                         dcc.Markdown("Il punteggio dei 3 Sottoindici è ottenuto dalla **media geometrica** dei punteggi delle **5 Dimensioni** che compongono ciascuno.", className="card-text")
                        ])
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Indice generale", className="card-title"),
                        dcc.Markdown("Il punteggio dell'Indice generale è ottenuto dalla **media geometrica** dei punteggi dei **3 Sottoindici** che lo compongono.", className="card-text")
                    ])
                )
            ]),
        align='center', lg= 6, xs =12)
    ],  justify="around")
])

