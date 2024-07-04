## Data Transformation - Market Research

This project module utilizes Pandas and SQLite to transform and store collected data about sports shoes from Mercado Livre. Below are the modules and functionalities used.

### Modules Used

#### `pandas`

Pandas is an essential library for data manipulation and analysis in Python. In the project, it is used to load, process, and analyze data from sports shoes.

- **`pd.read_json`**: Reads data from a JSON file and returns a DataFrame.
- **`df.head`**: Displays the first few rows of the DataFrame.
- **`df['column_name'].fillna`**: Fills null values in a column with a specified value.
- **`df['column_name'].astype`**: Converts the data type of a column.
- **`df['column_name'].str.replace`**: Replaces occurrences of a string pattern with another.
- **`df.drop`**: Removes columns or rows from the DataFrame.
- **`pd.options.display.max_columns`**: Configures the display of all columns in the DataFrame.

#### `sqlite3`

SQLite3 is a lightweight, self-contained SQL database. It is used in the project to store data about sports shoes.

- **`sqlite3.connect`**: Connects to the SQLite database.
- **`df.to_sql`**: Saves DataFrame data into an SQL database table.
- **`conn.close`**: Closes the connection to the database.

#### `datetime`

Python's `datetime` library provides classes for manipulating dates and times. It is used in the project to add a column with the current date and time to the data.

### Code Structure

The project code is structured as follows:

1. **Define Path to JSONL File**
    ```python
    jsonl_path = '../data/data.jsonl'
    ```

2. **Read Data from JSONL File**
    ```python
    df = pd.read_json(jsonl_path, lines=True)
    print(df.head())
    ```

3. **Add Fixed Columns and Collection Date**
    ```python
    df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"
    df['_collection_date'] = datetime.now()
    ```

4. **Handle Null Values and Numeric Columns**
    ```python
    df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
    df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
    df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
    df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
    df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)
    ```

5. **Remove Parentheses from `reviews_amount` Columns**
    ```python
    df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
    df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)
    ```

6. **Calculate Total Price Values**
    ```python
    df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
    df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100
    df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)
    ```

7. **Save Data to SQLite Database**
    ```python
    conn = sqlite3.connect('../data/quotes.db')
    df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)
    conn.close()
    ```

8. **Configure Pandas to Display All Columns**
    ```python
    pd.options.display.max_columns = None
    print(df.head())
    ```

### Running the Project

1. **Install Required Dependencies:**
    ```bash
    pip install pandas sqlite3
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd src/transformacao
    ```

3. **Execute the Data Transformation Script:**
    ```bash
    python process_data.py
    ```

### Description of Fields in the DataFrame

- **`_source`**: URL source from where the data was collected.
- **`_collection_date`**: Date and time when the data was collected.
- **`old_price`**: Old price calculated from `old_price_reais` and `old_price_centavos`.
- **`new_price`**: New price calculated from `new_price_reais` and `new_price_centavos`.
- **`reviews_rating_number`**: Average product rating.
- **`reviews_amount`**: Number of product reviews.