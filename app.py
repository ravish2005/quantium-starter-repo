import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Read data
df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f5f5f5",
        "padding": "30px",
        "fontFamily": "Arial",
    },
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            },
        ),

        html.Label(
            "Select Region:",
            style={"fontSize": "20px", "fontWeight": "bold"},
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"},
        ),

        dcc.Graph(id="sales-chart"),
    ],
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value"),
)
def update_graph(region):
    filtered = df.copy()

    if region != "all":
        filtered = filtered[filtered["region"] == region]

    sales = (
        filtered.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        sales,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white",
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)