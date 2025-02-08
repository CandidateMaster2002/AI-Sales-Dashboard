import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load sample data
df = pd.read_excel("Medical_Store_Sales_Analysis.xlsx")

def main():
    st.set_page_config(page_title="AI Sales Dashboard", layout="wide")
    st.title("📊 AI-Powered Sales & Inventory Dashboard")
    
    # Sales Overview
    col1, col2 = st.columns(2)
    total_sales = df['Total Revenue'].sum()
    total_profit = df['Profit'].sum()
    col1.metric("Total Sales (₹)", f"{total_sales:,.2f}")
    col2.metric("Total Profit (₹)", f"{total_profit:,.2f}")
    
    # Sales Trends
    st.subheader("📈 Sales Trends")
    df['Date'] = pd.to_datetime(df['Date'])
    sales_trend = df.groupby('Date').sum().reset_index()
    fig = px.line(sales_trend, x='Date', y='Total Revenue', title="Daily Sales Trend")
    st.plotly_chart(fig, use_container_width=True)
    
    # Top Customers
    st.subheader("🏆 Top Customers")
    top_customers = df.groupby('Customer')['Total Revenue'].sum().sort_values(ascending=False).head(5)
    st.table(top_customers)
    
    # Inventory Alerts (Random Data for Example)
    st.subheader("⚠️ Inventory Alerts")
    inventory_df = pd.DataFrame({
        "Product": ["Paracetamol", "Cough Syrup", "Vitamin C"],
        "Stock Remaining": [5, 2, 8]
    })
    st.table(inventory_df)
    
    # Smart Notifications
    st.subheader("📢 Smart Notifications")
    st.write("🔹 Restock **Cough Syrup** – Only 2 left!")
    st.write("🔹 Sales have increased by 15% this month!")

if __name__ == "__main__":
    main()
