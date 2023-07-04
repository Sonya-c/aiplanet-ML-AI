import dash
from dash import dcc, html

app = dash.Dash()

BACKGROUND_COLOR = "#090e2b"
TEXT_COLOR = "#7fdbff"

TEXT_STYLE = {
    "textAlign": "center",
    "color": TEXT_COLOR
}

data = [
    {
        "x": [1, 2, 3],
        "y": [4, 1, 2],
        "type": "bar",
        "name": "SF"
    },
    {
        "x": [1, 2, 3],
        "y": [2, 4, 5],
        "type": "bar",
        "name": "Montreal"
    },

]
app.layout = html.Div(
    style = {
        "backgroundColor": BACKGROUND_COLOR
    },
    children = [
        html.H1(
            children="Hello dash",
            style = TEXT_STYLE
        ),
        html.Div(
            children="Dash: A web application framework for Python.",
            style= TEXT_STYLE
        ),
        dcc.Graph(
            id="graph-01",
            figure = {
                "data": data,
                "layout": {
                    "plot_bgcolor": BACKGROUND_COLOR,
                    "paper_bgcolor": BACKGROUND_COLOR,
                    "font": {
                        "color": TEXT_COLOR
                    }
                }
            }
        )
    ] 
)

if __name__ == "__main__":
    app.run_server(debug=True)


