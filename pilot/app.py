import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('quotes.db')

df = pd.read_sql_query("SELECT * FROM quotes", conn)

conn.close()

st.title('Quotes Dashboard')

st.subheader('DataFrame')
st.write(df)

total_quotes = df.shape[0]
st.metric(label="Total Number of Quotes", value=total_quotes)

unique_authors = df['author'].nunique()
st.metric(label="Number of Unique Authors", value=unique_authors)

most_recent_collection = df['_collect_date'].max()
st.metric(label="Most Recent Collection Date", value=most_recent_collection)

st.subheader('Quotes by Author')
quotes_by_author = df['author'].value_counts()
st.bar_chart(quotes_by_author)

st.subheader('Some Quotes')
for index, row in df.iterrows():
    st.write(f"**{row['author']}**: {row['text']}")
