import pandas as pd
import numpy as np

from num2words import num2words as n2w

import plotly.express as px 
import plotly.io as pio
import plotly.graph_objects as go

data = pd.read_csv("../data/suicide-rate-1990-2017.csv")
print(data.head())

years = list(range(1990, 2017 + 1))
print(years)

dict_keys = [n2w(num) for num in range(1, len(years) + 1)]
print(dict_keys)

n_frame={}

for year, key in zip(years, dict_keys):
    df = data[(data["year"]==year)&(data["region"]=="Europe")]
    df = df.nlargest(n=5, columns=["suicide rate (deaths per 100,000)"])
    df = df.sort_values(by=["year", "suicide rate (deaths per 100,000)"])
    
    n_frame[key] = df

print(n_frame)

fig = go.Figure(
    data=[
        go.Bar(
            x = n_frame["one"]["suicide rate (deaths per 100,000)"],
            y = n_frame["one"]["country"],
            orientation="h",
            text=n_frame["one"]["suicide rate (deaths per 100,000)"],
            texttemplate="%{text:.3s}",
            textfont={"size": 18},
            textposition="inside",
            insidetextanchor="middle",
            width=0.9,
            marker={"color": n_frame["one"]["color_code"]}
        )
    ],
    layout=go.Layout(
        xaxis= dict(
            range=[0,60],
            autorange=False,
            title=dict(
                text="suicide rate (deaths per 100,000)"
            )
        ),
        yaxis= dict(
            range=[-0.5, 5.5],
            autorange=False,
            tickfont=dict(size = 14)
        ),
        title=dict(
                text="Suicide Rates per Country: 1990",
                font=dict(size=18),
                x=0.5,
                xanchor="center"
        ),

        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None, 
                            {
                                "frame": {
                                    "duration": 1000,
                                    "redraw": True
                                },
                                "Transition": {
                                    "duration": 250,
                                    "easing": "linear"
                                }
                            }
                        ]
                    )
                ]
            )
        ],
    ),
    
    frames=[
        go.Frame(
            data=[
                go.Bar(
                    x = value["suicide rate (deaths per 100,000)"],
                    y = value["country"],
                    orientation="h",
                    text=value["suicide rate (deaths per 100,000)"],
                    marker={"color": value["color_code"]}
                )
            ],
            layout=go.Layout(
                xaxis= dict(
                    range=[0,60],
                    autorange=False,
                ),
                yaxis= dict(
                    range=[-0.5, 5.5],
                    autorange=False,
                    tickfont=dict(size = 14)
                ),
                title=dict(
                    text="Suicide Rates per Country: " +
                    str(value["year"].values[0]),
                    font=dict(size=18),
                ),
            )
        )
        for key, value in n_frame.items()
    ]
)
fig.write_html("07_racing.html", auto_open=True)

