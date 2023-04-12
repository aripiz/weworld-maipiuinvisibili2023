# render_tab.py

from index import app
from dash import Input, Output

from layout.data_tabs import tab_map_features, tab_map_indicators, tab_correlations, tab_ranking, tab_evolution, tab_radar

# Tabs
@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"))
def render_tab(active_tab):
    if active_tab is not None:
        if active_tab == "map_features": return tab_map_features
        elif active_tab == "map_indicators":  return tab_map_indicators
        elif active_tab == "correlations": return tab_correlations
        elif active_tab == 'ranking': return tab_ranking
        elif active_tab == 'evolution': return tab_evolution
        elif active_tab == 'radar': return tab_radar
    return "Nessun elemento selezionato."
