import streamlit as st
import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('../data/quotes.db')

# Load data from the 'mercadolivre_items' table into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

# Close the database connection
conn.close()

# Application title
st.title('Market Research - Sports Shoes on Mercado Livre')

# Improve layout with columns for KPIs
st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)

# KPI 1: Total number of items
total_items = df.shape[0]
col1.metric(label="Total Number of Items", value=total_items)

# KPI 2: Number of unique brands
unique_brands = df['brand'].nunique()
col2.metric(label="Number of Unique Brands", value=unique_brands)

# KPI 3: Average new price (in BRL)
average_new_price = df['new_price'].mean()
col3.metric(label="Average New Price (R$)", value=f"{average_new_price:.2f}")

# Top brands found up to the 10th page
st.subheader('Top Brands Found up to the 10th Page')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df.head(500)['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Average price by brand
st.subheader('Average Price by Brand')
col1, col2 = st.columns([4, 2])
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Satisfaction by brand
st.subheader('Satisfaction by Brand')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)
