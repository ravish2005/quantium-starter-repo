import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Read processed data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Group sales by date
sales = df.groupby("date", as_index=False)["sales"].sum()

# Create line chart
fig = px.line(
    sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)