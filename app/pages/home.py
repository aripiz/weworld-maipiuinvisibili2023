# home.py

from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from index import TITLE

register_page(__name__, path='/', name=TITLE)

# Home map
import plotly.express as px
import plotly.io as pio
import pandas as pd
from dash_bootstrap_templates import load_figure_template
from index import df_data
from index import MAP_STYLE, MAP_TOKEN, GEO_FILE, FIGURE_TEMPLATE, COLOR_SCALE
load_figure_template(FIGURE_TEMPLATE)
pio.templates.default = FIGURE_TEMPLATE

def display_map_home():
    df = df_data[df_data['area'].notna()].copy()
    bins = [0, 45, 55, 65, 75, 85, 100] 
    tier_labels = ['Esclusione molto grave', 'Esclusione grave', 'Inclusione insufficiente', 'Inclusione sufficiente', 'Inclusione buona', 'Inclusione molto buona']
    df['Livello'] = pd.cut(df['Generale'], bins=bins, labels=tier_labels, right=False).cat.remove_unused_categories()
    fig = px.choropleth_mapbox(df.loc[df['anno']==2022], geojson=GEO_FILE,
        locations='codice_istat', featureidkey="properties.istat_code_num",
        color='Livello',
        #range_color=[20,80],
        color_discrete_sequence=COLOR_SCALE,
        category_orders={'Livello': tier_labels[:-2]},
        hover_name='territorio',
        hover_data={'codice_istat':False, 'anno': False,
                    'Generale': ':.3g', 'Contesto':':.3g', 'Bambini':':.3g', 'Donne':':.3g'},
        zoom=4.5, opacity=1, center=dict(lat=42, lon=12)
    )
    fig.update_layout(coloraxis_colorbar=dict(title="Livello", x=0.92))
    fig.update_layout(
        mapbox_style = MAP_STYLE,
        mapbox_accesstoken = MAP_TOKEN,
        margin={"r":0,"t":30,"l":0,"b":0},
    )
    return fig

layout = html.Div([
        dbc.Row(dbc.Col(dcc.Markdown("## L’Indice _Mai più invisibili_"))),
        html.Br(),
        dbc.Row([
            dbc.Col([
                #dcc.Markdown("### Il diritto all'inclusione"),
                dcc.Markdown(
                "In un mondo in cui le diseguaglianze permangono e la povertà è ancora un problema globale, donne, bambini, bambine e adolescenti sono ovunque le categorie di persone più a rischio di esclusione sociale. Per questo, il primo obiettivo di WeWorld è la **promozione del diritto all’inclusione di donne, bambini e giovani in Italia e nel mondo.**"),
                dcc.Markdown(
                "Condizione imprescindibile per realizzare azioni di inclusione e proporre politiche sociali è conoscere il più possibile le loro condizioni di vita e i rischi di emarginazione sociale a cui vanno incontro. L’Indice biennale **_Mai più invisibili_ sulla condizione di donne, bambini e adolescenti in Italia**, pubblicato per la prima volta nel 2020, **nasce dall’esigenza di valutare in quali ambiti vi sono forme di inclusione/esclusione a livello regionale.**"),
                dcc.Markdown(
                "L’Italia viene monitorata nella sua capacità di garantire e promuovere i diritti di queste categorie sociali attraverso una serie di **30 Indicatori**, raggruppati in **15 Dimensioni**, a loro volta divise in **3 Sottoindici**: Contesto, Bambini e Donne che aggregati forniscomo un **Indice generale.**"),
                dbc.Card(
                    dbc.CardBody([    
                        #dcc.Markdown("**L’Indice Mai più invisibili:**"),
                        dbc.ListGroup([
                            dbc.ListGroupItem("Valuta il progresso dei territori alla luce delle condizioni di inclusione che riescono a garantire alle categorie più vulnerabili: donne, bambini e adolescenti."),
                            dbc.ListGroupItem("Tiene conto delle condizioni di donne e minori in maniera congiunta, interdipendente e simultanea, riconoscendo un nesso tra l’implementazione dei diritti di una categoria sul benessere dell’altra e viceversa."),
                            dbc.ListGroupItem("Considera il concetto di inclusione al di là di un’accezione dello sviluppo puramente economicistica, aprendo a una visione ampia, multidimensionale, dinamica e positiva, personale, sociale e intersezionale, universale.") #(in linea con l’Agenda 2030 e le cosiddette 5P: People, Planet, Prosperity, Partnership, Peace)
                        ], flush=True)]))
            ],),
           dbc.Col(dcc.Graph(figure=display_map_home(), responsive=True, style ={"height":"70vh"}), align='center')        
        ],
        justify='evenly'),
        # html.Br(),
        # dbc.Row([
        #     dbc.Col([
        #         dcc.Markdown("### Perché tre sottoindici?"),
        #         dcc.Markdown(
        #         "La metodologia adottata consente di produrre classifiche delle 19 Regioni e 2 Province Autonome considerate anche per i tre sottoindici (Contesto, Bambini e Donne) che compongono l’Indice generale. La necessità di valutare separatamente le performance dei territori in relazioni ai tre sottoindici nasce da un assunto ben preciso: intervenire per garantire inclusione tout court, senza tenere conto degli specifici bisogni e rischi di genere e generazionali, adottando dunque un approccio intersezionale, non consente una piena realizzazione dei diritti e delle capacitazioni di donne, bambini/e e adolescenti. **Una reale inclusione di queste categorie, infatti, può compiersi solo attraverso la creazione, implementazione e il monitoraggio di policy adeguate che devono essere al tempo stesso multidimensionali, per tenere conto dell’intreccio esistente tra i diritti di donne e minori, e targettizzate, ovvero tarate sulle loro necessità specifiche.** L’Italia offre un contesto tendenzialmente favorevole (pur con le dovute differenze geografiche) all’inclusione delle categorie più vulnerabili, eppure queste continuano a vivere in condizioni di svantaggio e fragilità. **Per questo è necessario guardare ancora più da vicino alle loro condizioni.** In effetti, i valori ottenuti dalle regioni nei tre sottoindici sono in certi casi molto diversi, al punto da apparire quasi discordanti. **Questo ci rammenta della necessità di procedere su due fronti paralleli e complementari: da una parte è fondamentale lavorare sui contesti in cui donne, bambini/e e adolescenti vivono e renderli il più favorevoli possibile al loro pieno sviluppo, diritti e inclusione; dall’altra non si può di certo pensare che contesti favorevoli siano di per sé sufficienti a soddisfare i bisogni e le istanze di donne, bambini/e e adolescenti, per i quali sono necessarie politiche adeguate e interventi mirati.**"),
        #     ]),
        #     dbc.Col([dbc.Row([
        #         dbc.Col(dbc.Card(
        #             dbc.CardBody([
        #                 html.H4("Contesto", className="card-title"),
        #                 dbc.ListGroup([ dbc.ListGroupItem(dim, style={'height':'65px', }) for dim in df_meta.loc[[1,3,5,7,9],'dimensione']],
        #                 numbered=False, flush=True,
        #                 className="card-text",)
        #                 ])
        #         )),
        #         dbc.Col(dbc.Card(
        #             dbc.CardBody([
        #                 html.H4("Bambini", className="card-title"),
        #                 dbc.ListGroup([ dbc.ListGroupItem(dim, style={'height':'65px'}) for dim in df_meta.loc[[11,13,15,17,19],'dimensione']],
        #                 numbered=False, flush=True,
        #                 className="card-text",)
        #                 ])
        #         )),
        #         dbc.Col(dbc.Card(
        #             dbc.CardBody([
        #                 html.H4("Donne", className="card-title"),
        #                 dbc.ListGroup([ dbc.ListGroupItem(dim, style={'height':'65px'}) for dim in df_meta.loc[[21,23,25,27,29],'dimensione']],
        #                 numbered=False, flush=True,
        #                 className="card-text",)
        #             ]))),
        #     ], justify="evenly")
        #     ], align='center'),
        # ], justify="evenly")
    ])