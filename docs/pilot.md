# Pilot Project

## Extraction, Transformation, and Load

```python
import scrapy
import pandas as pd
import sqlite3
from datetime import datetime
import streamlit as st

# Extraction
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# Run the spider
from scrapy.crawler import CrawlerProcess
process = CrawlerProcess(settings={
    "FEEDS": {
        "quotes.csv": {"format": "csv"},
    },
})
process.crawl(QuotesSpider)
process.start()

# Transformation and Load
# Define the source variable
source = "quotes_scrapy"

# Load the CSV into a pandas DataFrame
df = pd.read_csv('quotes.csv')

# Add the _source column
df['_source'] = source

# Add the _collection_date column with the current date and time
df['_collection_date'] = datetime.now()

# Connect to the SQLite database (or create a new one)
conn = sqlite3.connect('quotes.db')

# Save the DataFrame to the SQLite database
df.to_sql('quotes', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

# Dashboard
# Connect to the SQLite database
conn = sqlite3.connect('quotes.db')

# Load the data from the 'quotes' table into a pandas DataFrame
df = pd.read_sql_query("SELECT * FROM quotes", conn)

# Close the database connection
conn.close()

# Application title
st.title('Quotes Dashboard')

# Show the DataFrame
st.subheader('DataFrame')
st.write(df)

# KPI 1: Total number of quotes
total_quotes = df.shape[0]
st.metric(label="Total Number of Quotes", value=total_quotes)

# KPI 2: Number of unique authors
unique_authors = df['author'].nunique()
st.metric(label="Number of Unique Authors", value=unique_authors)

# KPI 3: Most recent collection date
most_recent_collection = df['_collection_date'].max()
st.metric(label="Most Recent Collection Date", value=most_recent_collection)

# Show quotes by author
st.subheader('Quotes by Author')
quotes_by_author = df['author'].value_counts()
st.bar_chart(quotes_by_author)

# Show some quotes
st.subheader('Some Quotes')
for index, row in df.iterrows():
    st.write(f"**{row['author']}**: {row['text']}")
```

```bash
streamlit run app.py
```