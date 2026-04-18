import pandas as pd

def load_data():
    df = pd.read_csv("data/sales_data.csv")
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)
    df['total_amount'] = df['price'] * df['quantity']
    df['date'] = pd.to_datetime(df['date'])
    return df