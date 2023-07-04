import dash
from dash import Input, Output, dcc, html, callback

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id="input",
        value="dash app",
        type="text"
    ),
    html.Div(
        id="div"
    )
])

@callback(
    Output(
        component_id="div",
        component_property="children"
    ),
    Input(
        component_id="input",
        component_property="value"
    )
)
def update_output_div(input_value):
    return "You have entered " + str(input_value)

if __name__ == "__main__":
    app.run_server(debug=True)


