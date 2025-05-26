import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Sales Data Analyzer", layout="centered")

st.markdown("<h1 style='text-align:center; color:#4CAF50;'>Sales Data Analyzer App</h1>", unsafe_allow_html=True)

# Session state for storing data
if 'df' not in st.session_state:
    np.random.seed(42)
    num_days = 30
    dates = pd.date_range(start="2024-01-01", periods=num_days)
    products = ['Laptop', 'Phone', 'Tablet', 'Headphones']
    sales_data = {
        'Date': dates,
        'Product': np.random.choice(products, num_days),
        'Units Sold': np.random.randint(5, 50, num_days),
        'Price per Unit': np.random.randint(5000, 50000, num_days)
    }
    st.session_state.df = pd.DataFrame(sales_data)
    st.session_state.df['Total Sales'] = st.session_state.df['Units Sold'] * st.session_state.df['Price per Unit']

# Reset button
if st.button("🔁 Reset to Original Data"):
    np.random.seed(42)
    num_days = 30
    dates = pd.date_range(start="2024-01-01", periods=num_days)
    products = ['Laptop', 'Phone', 'Tablet', 'Headphones']
    sales_data = {
        'Date': dates,
        'Product': np.random.choice(products, num_days),
        'Units Sold': np.random.randint(5, 50, num_days),
        'Price per Unit': np.random.randint(5000, 50000, num_days)
    }
    st.session_state.df = pd.DataFrame(sales_data)
    st.session_state.df['Total Sales'] = st.session_state.df['Units Sold'] * st.session_state.df['Price per Unit']
    st.success("Data has been reset!")

# Form to add new data
with st.form("add_entry"):
    st.markdown("### ➕ Add a New Sales Entry")
    c1, c2 = st.columns(2)

    with c1:
        new_date = st.date_input("Date")
        new_product = st.selectbox("Product", ['Laptop', 'Phone', 'Tablet', 'Headphones'])

    with c2:
        new_units = st.number_input("Units Sold", min_value=1, step=1)
        new_price = st.number_input("Price per Unit", min_value=1000, step=100)

    submit = st.form_submit_button("Add Entry")

    if submit:
        new_row = {
            'Date': new_date,
            'Product': new_product,
            'Units Sold': new_units,
            'Price per Unit': new_price,
            'Total Sales': new_units * new_price
        }
        st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_row])], ignore_index=True)
        st.success("New entry added!")

# Show data
df = st.session_state.df.copy()
st.markdown("## 📊 Current Sales Data")
st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)

# Analysis
total_revenue = df['Total Sales'].sum()
avg_sales_per_day = df['Total Sales'].mean()
best_selling_product = df.groupby('Product')['Total Sales'].sum().idxmax()

st.markdown("## 📈 Analysis")
st.write(f"*Total Revenue:* ₹{total_revenue:,.2f}")
st.write(f"*Average Sales per Entry:* ₹{avg_sales_per_day:,.2f}")
st.write(f"*Best Selling Product:* {best_selling_product}")

# Visualization: Sales Trend
st.markdown("### Daily Sales Trend")
fig1, ax1 = plt.subplots()
df.groupby('Date')['Total Sales'].sum().plot(ax=ax1, marker='o', color='teal')
ax1.set_xlabel("Date")
ax1.set_ylabel("Total Sales")
ax1.set_title("Sales Trend Over Time")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Visualization: Sales by Product
st.markdown("### Total Sales by Product")
fig2, ax2 = plt.subplots()
df.groupby('Product')['Total Sales'].sum().plot(kind='bar', ax=ax2, color='coral')
ax2.set_xlabel("Product")
ax2.set_ylabel("Total Sales")
ax2.set_title("Total Sales by Product")
st.pyplot(fig2)