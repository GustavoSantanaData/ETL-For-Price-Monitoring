# Dashboard Documentation

## Market Research - Sports Shoes on Mercado Livre

This project uses Streamlit to create an interactive application that analyzes data on sports shoes from Mercado Livre. Below are the modules and functionalities used.

### Modules Used

#### `streamlit`

Streamlit is an open-source framework that allows creating interactive web applications in Python quickly and easily. Below are the main Streamlit components used in the project:

- **`st.title`**: Sets the application title.
- **`st.subheader`**: Sets a subtitle for the application sections.
- **`st.columns`**: Creates a column layout, allowing the application elements to be organized side by side.
- **`st.metric`**: Displays KPIs (Key Performance Indicators) in a visually appealing way.
- **`st.bar_chart`**: Creates bar charts for data visualization.
- **`st.write`**: Displays tables and other types of data.

#### `pandas`

Pandas is an essential library for data manipulation and analysis in Python. In the project, it is used to load, process, and analyze the sports shoes data.

- **`pd.read_sql_query`**: Reads data from an SQL table and returns a DataFrame.
- **`df.shape`**: Returns the number of rows and columns in the DataFrame.
- **`df['column_name'].nunique`**: Counts the number of unique values in a column.
- **`df['column_name'].mean`**: Calculates the mean of the values in a column.
- **`df['column_name'].value_counts`**: Counts the frequency of unique values in a column.
- **`df.groupby('column_name').mean`**: Groups the data by a column and calculates the mean for each group.
- **`df.sort_values`**: Sorts the values in a DataFrame.

#### `sqlite3`

SQLite3 is a lightweight, self-contained SQL database. It is used in the project to store the sports shoes data.

- **`sqlite3.connect`**: Connects to the SQLite database.
- **`pd.read_sql_query`**: Executes an SQL query and returns the results as a DataFrame.

### Code Structure

The project code is structured as follows:

1. **Connect to the Database**
    ```python
    conn = sqlite3.connect('../data/quotes.db')
    df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)
    conn.close()
    ```

2. **Application Title**
    ```python
    st.title('Market Research - Sports Shoes on Mercado Livre')
    ```

3. **Main KPIs**
    ```python
    st.subheader("Main KPIs")
    col1, col2, col3 = st.columns(3)

    total_items = df.shape[0]
    col1.metric(label="Total Number of Items", value=total_items)

    unique_brands = df['brand'].nunique()
    col2.metric(label="Number of Unique Brands", value=unique_brands)

    average_new_price = df['new_price'].mean()
    col3.metric(label="Average New Price (R$)", value=f"{average_new_price:.2f}")
    ```

4. **Specific Analyses**
    - **Most Found Brands up to the 10th Page**
        ```python
        st.subheader('Most Found Brands up to the 10th Page')
        col1, col2 = st.columns([4, 2])
        top_10_pages_brands = df.head(500)['brand'].value_counts().sort_values(ascending=False)
        col1.bar_chart(top_10_pages_brands)
        col2.write(top_10_pages_brands)
        ```

    - **Average Price by Brand**
        ```python
        st.subheader('Average Price by Brand')
        col1, col2 = st.columns([4, 2])
        average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
        col1.bar_chart(average_price_by_brand)
        col2.write(average_price_by_brand)
        ```

    - **Satisfaction by Brand**
        ```python
        st.subheader('Satisfaction by Brand')
        col1, col2 = st.columns([4, 2])
        df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
        satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
        col1.bar_chart(satisfaction_by_brand)
        col2.write(satisfaction_by_brand)
        ```

### How to Run the Project

1. **Install the necessary dependencies:**
    ```bash
    pip install streamlit pandas sqlite3
    ```

2. **Navigate to the project directory:**
    ```bash
    cd src/dashboard
    ```

3. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

4. **Access the application in your browser:**
    Open `http://localhost:8501` in your browser to view the Streamlit application.
