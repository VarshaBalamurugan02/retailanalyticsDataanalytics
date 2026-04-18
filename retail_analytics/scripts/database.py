import sqlite3

def connect_db():
    return sqlite3.connect("sales.db")

def setup_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        order_id INTEGER,
        product TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        city TEXT,
        date TEXT,
        total_amount REAL
    )
    """)

def insert_data(conn, df):
    df.to_sql("sales", conn, if_exists="replace", index=False)

def sql_city_sales(conn):
    result = conn.execute("""
    SELECT city, SUM(total_amount)
    FROM sales
    GROUP BY city
    """)
    return result.fetchall()