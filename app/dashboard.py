import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

df = pd.read_csv("data/cleaned_retail.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# KPI metrics
total_revenue = df["Revenue"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()
avg_order_value = total_revenue / total_orders

st.title("Interactive Sales Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# Revenue trend
revenue_trend = (
    df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

fig1 = px.line(revenue_trend, x="Month", y="Revenue", title="Monthly Revenue Trend")

st.plotly_chart(fig1, use_container_width=True)

# Top products
top_products = (
    df.groupby("Description")["Revenue"]
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
    title="Top Products"
)

st.plotly_chart(fig2, use_container_width=True)

# Sales by country
sales_country = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig3 = px.bar(
    sales_country,
    x="Country",
    y="Revenue",
    title="Top Countries by Revenue"
)

st.plotly_chart(fig3, use_container_width=True)
