import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales data in dictionary format
sales_data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'Category': ['Category X', 'Category Y', 'Category X', 'Category Z', 'Category Y'],
    'Quantity': [3, 2, 5, 1, 4],
    'Revenue': [150, 120, 250, 50, 180],
    'Order_Date': ['2023-01-15', '2023-02-20', '2023-01-30', '2023-03-10', '2023-02-28']
}

# Create a DataFrame from the sample data
df = pd.DataFrame(sales_data)

# Convert 'Order_Date' column to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Set seaborn style for better visualizations
sns.set(style='whitegrid', palette='pastel')

# Streamlit UI
st.title("Sales Data Analysis")

# Line Plot: Monthly Sales Trends
st.subheader("Monthly Sales Trends")
fig1, ax1 = plt.subplots()
monthly_sales = df.set_index('Order_Date')['Revenue'].resample('M').sum()
sns.lineplot(data=monthly_sales, marker='o', ax=ax1)
ax1.set_xlabel("Date")
ax1.set_ylabel("Revenue ($)")
st.pyplot(fig1)

# Bar Plot: Sales by Category
st.subheader("Sales by Category")
fig2, ax2 = plt.subplots()
sns.barplot(data=df, x='Category', y='Revenue', ci=None, ax=ax2)
ax2.set_xlabel("Category")
ax2.set_ylabel("Revenue ($)")
st.pyplot(fig2)

# Pie Chart: Sales Distribution by Product
st.subheader("Sales Distribution by Product")
fig3, ax3 = plt.subplots()
sales_by_product = df.groupby('Product')['Revenue'].sum()
ax3.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=90)
st.pyplot(fig3)

# Pie Chart: Sales Distribution by Category
st.subheader("Sales Distribution by Category")
fig4, ax4 = plt.subplots()
sales_by_category = df.groupby('Category')['Revenue'].sum()
ax4.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%', startangle=90)
st.pyplot(fig4)
