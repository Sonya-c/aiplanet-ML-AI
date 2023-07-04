import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

# -------------------------------------------------------------------------
# DATA 
data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/intro_bees.csv")

data = data.groupby([
    "State",
    "ANSI",
    "Affected by",
    "Year",
    "state_code"
])[["Pct of Colonies Impacted"]].mean()

data.reset_index(inplace=True)

print("Data (head)\n", data.head())

# -------------------------------------------------------------------------
# APP
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div([
    html.H1(
        "Web Aplication Dashboards with Dash",
        style={
            "textAlign": "center"
        }
    ),
    html.H3(
        id="output-container",
        children=[],
        style={
            "textAlign": "center"
        }
    ),
    dcc.Graph(
        id="graph",
        figure={}
    ),
    html.Br(),
    dcc.Slider(0, len(data.Year.unique()) - 1, 1,
        id="input-year",
        marks={ 
            key: str(year) 
            for key, year 
            in enumerate(data.Year.unique())
        },
        tooltip={
            "placement": "top",
        },
        value=0,
    )
])

@callback(
    Output(
        component_id="output-container",
        component_property="children"
    ),
    Output(
        component_id="graph",
        component_property="figure"
    ),
    Input(
        component_id="input-year",
        component_property="value"
    )
)
def update_graph(index_selected):

    year_selected = data.Year.unique()[index_selected]

    data_sub = data.copy()
    data_sub = data_sub[data_sub["Year"] == year_selected]

    fig = px.choropleth(
        data_sub,
        locationmode="USA-states",
        locations="state_code",
        scope="usa",
        color="Pct of Colonies Impacted",
        hover_data=["State", "Pct of Colonies Impacted"],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={"Pct of Colonies Impacted":"% of Bee Colonies"},
        template="plotly_dark"
    )

    return f"% of Bee Colonies per State({year_selected})", fig 

if __name__ == "__main__":
    app.run_server(debug=True)

    
