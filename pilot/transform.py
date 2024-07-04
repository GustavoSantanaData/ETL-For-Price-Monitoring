import pandas as pd
import sqlite3
from datetime import datetime

source = "quotes_scrapy"

df = pd.read_csv('quotes.csv')

df['_source'] = source
df['_collection_date'] = datetime.now()

conn = sqlite3.connect('quotes.db')
df.to_sql('quotes', conn, if_exists='replace', index=False)
conn.close()
