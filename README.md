# Interactive Sales Analytics Dashboard

## Overview

This project builds an interactive sales analytics dashboard using Python and Streamlit.

The dashboard analyzes retail transaction data and provides insights into revenue trends, top products, and top countries by sales.

The goal of this project is to demonstrate practical data analytics and dashboard development skills used in real business environments.

---

## Features

The dashboard includes the following key business metrics:

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value

Interactive visualizations include:

* Monthly Revenue Trend
* Top 10 Products by Revenue
* Top 10 Countries by Revenue

The dashboard allows users to explore sales performance and identify key trends in the data.

---

## Technologies Used

Python
Pandas
Streamlit
Plotly

---

## Project Structure

interactive-sales-dashboard-khatantamir

app/
  dashboard.py

data/
  cleaned_retail.csv

notebooks/
  eda.ipynb

src/
  data_cleaning.py
  metrics.py
  charts.py

requirements.txt
README.md
dashboard_preview.png

---

## How to Run the Dashboard

Clone the repository:

git clone https://github.com/Khatantamir/interactive-sales-dashboard-khatantamir.git

Move into the project folder:

cd interactive-sales-dashboard-khatantamir

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

python -m streamlit run app/dashboard.py

Then open the following URL in your browser:

http://localhost:8501

---

## Dashboard Preview

![Dashboard Preview](dashboard_preview.png)

---

## Business Insights Example

Using this dashboard we can quickly observe:

* Monthly revenue trends across the year
* The best performing products
* The countries generating the most revenue

These insights help businesses understand customer demand and optimize product strategy.

---

## Author

Khatantamir Otgonbyamba
