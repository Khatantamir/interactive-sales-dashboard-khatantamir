import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/cleaned_retail.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

st.title("Interactive Sales Analytics Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

country_options = ["All"] + sorted(df["Country"].dropna().unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", country_options)

min_date = df["InvoiceDate"].min().date()
max_date = df["InvoiceDate"].max().date()

start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

# Apply filters
filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]

filtered_df = filtered_df[
    (filtered_df["InvoiceDate"].dt.date >= start_date) &
    (filtered_df["InvoiceDate"].dt.date <= end_date)
]

# KPI metrics
total_revenue = filtered_df["Revenue"].sum()
total_orders = filtered_df["InvoiceNo"].nunique()
total_customers = filtered_df["CustomerID"].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# Revenue trend
revenue_trend = (
    filtered_df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    revenue_trend,
    x="Month",
    y="Revenue",
    title="Monthly Revenue Trend"
)
st.plotly_chart(fig1, use_container_width=True)

# Top products
top_products = (
    filtered_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    top_products,
    x="Revenue",
    y="Description",
    orientation="h",
    title="Top 10 Products"
)
st.plotly_chart(fig2, use_container_width=True)

# Top countries
sales_country = (
    filtered_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    sales_country,
    x="Country",
    y="Revenue",
    title="Top 10 Countries by Revenue"
)
st.plotly_chart(fig3, use_container_width=True)
