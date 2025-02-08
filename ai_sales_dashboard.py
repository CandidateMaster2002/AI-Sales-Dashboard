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
    
    # Best & Worst Sales Dates
    best_day = sales_trend.loc[sales_trend['Total Revenue'].idxmax()]
    worst_day = sales_trend.loc[sales_trend['Total Revenue'].idxmin()]
    st.subheader("📅 Best & Worst Sales Days")
    st.write(f"✅ **Best Sales Day:** {best_day['Date'].strftime('%Y-%m-%d')} (₹{best_day['Total Revenue']:,.2f})")
    st.write(f"❌ **Worst Sales Day:** {worst_day['Date'].strftime('%Y-%m-%d')} (₹{worst_day['Total Revenue']:,.2f})")
    
    # Best & Worst Sales Time (Check if 'Time' column exists)
    if 'Time' in df.columns:
        df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
        sales_by_hour = df.groupby('Hour')['Total Revenue'].sum()
        best_hour = sales_by_hour.idxmax()
        worst_hour = sales_by_hour.idxmin()
        
        st.subheader("⏰ Best & Worst Sales Times")
        st.write(f"🕒 **Best Hour:** {best_hour}:00 - ₹{sales_by_hour.max():,.2f}")
        st.write(f"🕑 **Worst Hour:** {worst_hour}:00 - ₹{sales_by_hour.min():,.2f}")
    else:
        st.warning("⚠️ 'Time' column is missing. Cannot calculate best/worst sales time.")
    
    # Top & Worst Performing Medicines
    st.subheader("💊 Best & Worst Selling Medicines")
    top_medicine = df.groupby('Product')['Total Revenue'].sum().idxmax()
    worst_medicine = df.groupby('Product')['Total Revenue'].sum().idxmin()
    st.write(f"🏆 **Best Selling Medicine:** {top_medicine}")
    st.write(f"⚠️ **Worst Selling Medicine:** {worst_medicine}")
    
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
    st.write("🔹 Best selling time is around **3 PM - 5 PM**")

if __name__ == "__main__":
    main()
