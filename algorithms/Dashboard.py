import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


df = pd.read_csv(r"C:/Users/Namit Yadav/Downloads/final_chosen_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

# 1️⃣ Sales Over Time
sales_over_time = px.line(
    df.groupby("Date")["Total Amount"].sum().reset_index(),
    x="Date", y="Total Amount",
    title="Sales Over Time"
)

# 2️⃣ Sales by Product Category
sales_by_category = px.bar(
    df.groupby("Product Category")["Total Amount"].sum().reset_index(),
    x="Product Category", y="Total Amount",
    title="Total Sales by Product Category"
)

# 3️⃣ Quantity Sold by Category
quantity_by_category = px.bar(
    df.groupby("Product Category")["Quantity"].sum().reset_index(),
    x="Quantity", y="Product Category",
    orientation="h",
    title="Top Categories by Quantity Sold"
)

# 4️⃣ Gender-wise Revenue
gender_pie = px.pie(
    df, names="Gender", values="Total Amount",
    title="Gender-wise Contribution to Sales"
)

# 5️⃣ Scatter: Age vs Spending
age_scatter = px.scatter(
    df, x="Age", y="Total Amount",
    size="Total Amount", color="Gender",
    title="Customer Age vs Amount Spent"
)

# 6️⃣ Age Distribution
age_hist = px.histogram(
    df, x="Age", nbins=15,
    title="Distribution of Customer Age"
)

# 7️⃣ Correlation Heatmap (Retail Metrics)
corr_fig = px.imshow(
    df[["Age", "Quantity", "Price per Unit", "Total Amount"]].corr(),
    color_continuous_scale="Viridis",
    title="Correlation Heatmap of Retail Metrics"
)

app.layout = html.Div([
    html.H1("Retail Insights Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(figure=sales_over_time),
    dcc.Graph(figure=sales_by_category),
    dcc.Graph(figure=quantity_by_category),
    dcc.Graph(figure=gender_pie),
    dcc.Graph(figure=age_scatter),
    dcc.Graph(figure=age_hist),
    dcc.Graph(figure=corr_fig)
])

app.run(debug=True)
