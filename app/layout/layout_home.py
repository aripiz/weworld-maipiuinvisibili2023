# data_home.py

import plotly.express as px
import plotly.io as pio
import pandas as pd
from dash_bootstrap_templates import load_figure_template
from index import df_data
from configuration import MAP_STYLE, MAP_TOKEN, GEO_FILE, FIGURE_TEMPLATE, COLOR_SCALE
load_figure_template(FIGURE_TEMPLATE)
pio.templates.default = FIGURE_TEMPLATE

# Home map
def display_map_home():
    df = df_data[df_data['area'].notna()].copy()
    bins = [0, 45, 55, 65, 75, 85, 100] 
    tier_labels = ['Esclusione molto grave', 'Esclusione grave', 'Inclusione insufficiente', 'Inclusione sufficiente', 'Inclusione buona', 'Inclusione molto buona']
    df['Livello'] = pd.cut(df['Generale'], bins=bins, labels=tier_labels, right=False).cat.remove_unused_categories()
    fig = px.choropleth_mapbox(df.loc[df['anno']==2022], geojson=GEO_FILE,
        locations='codice_istat', featureidkey="properties.istat_code_num",
        color='Livello',
        #range_color=[20,80],
        color_discrete_map=dict(zip(tier_labels,COLOR_SCALE)),
        category_orders={'Livello': tier_labels},
        hover_name='territorio',
        hover_data={'codice_istat':False, 'anno': False,
                    'Generale': ':.3g', 'Contesto':':.3g', 'Bambini':':.3g', 'Donne':':.3g'},
        zoom=4.5, opacity=1, center=dict(lat=42, lon=12)
    )
    fig.update_layout(legend=dict(title_text="Livelli d'inclusione/esclusione",xanchor='right', yanchor='top', x=0.95, y=0.95))
    fig.update_layout(
        mapbox_style = MAP_STYLE,
        mapbox_accesstoken = MAP_TOKEN,
        margin={"r":0,"t":30,"l":0,"b":0},
    )
    return fig