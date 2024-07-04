import pandas as pd
import sqlite3
from datetime import datetime

# Define the path to the JSONL file
jsonl_path = '../data/data.jsonl'

# Read data from the JSONL file
df = pd.read_json(jsonl_path, lines=True)

# Display the resulting DataFrame
print(df.head())

# Add the _source column with a fixed value
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

# Add the _collect_date column with the current date and time
df['_collect_date'] = datetime.now()

# Handle missing values for numeric and text columns
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Remove parentheses from the `reviews_amount` column
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

# Convert prices to floats and calculate total values
df['old_price'] = df['old_price_reais'] + df['old_price_cents'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_cents'] / 100

# Remove old price columns
df.drop(columns=['old_price_reais', 'old_price_cents', 'new_price_reais', 'new_price_cents'], inplace=True)

# Connect to the SQLite database (or create a new one)
conn = sqlite3.connect('../data/quotes.db')

# Save the DataFrame to the SQLite database
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Close the connection to the database
conn.close()

# Set pandas to display all columns
pd.options.display.max_columns = None

# Display the resulting DataFrame
print(df.head())
