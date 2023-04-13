# home.py

from dash import html, dcc, register_page
import dash_bootstrap_components as dbc
from index import TITLE

register_page(__name__, path='/', name=TITLE)

from layout.data_home import display_map_home

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