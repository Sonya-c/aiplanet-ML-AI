import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.io as pio
import plotly.graph_objects as go

data = pd.read_csv("../data/female_labour_cleaned.csv")
data = data[data["Continent"].isin(["Africa", "Europe"])]
data = data[data["Year"].isin(["1990", "1995", "2000", "2005"])]
data["resized_population"] = data["population"] / 10 ** 8
print(data.head())

fig = px.scatter_3d(
    data,
    x="GDP per capita",
    y="% Econ. active",
    z="Years in school (avg)",

    title="Female labor force participation analysis",

    color="Continent",
    color_discrete_sequence=["violet", "cyan"],
    template="plotly_dark",

    height=700,
    log_x=True, 

    hover_name="Entity",
    hover_data={"Continent": False, "GDP per capita": ":.lf"} ,

    size="resized_population",
    size_max=50,

    animation_frame="Year",
    range_x=[500, 100000],
    range_z=[0, 14],
    range_y=[5, 100],
)

fig.write_html("figure.html", auto_open=True)
