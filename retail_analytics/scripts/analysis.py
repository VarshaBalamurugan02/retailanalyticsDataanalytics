import numpy as np

def get_total_sales(df):
    return np.sum(df['total_amount'])

def get_top_product(df):
    return df.groupby('product')['total_amount'].sum().idxmax()

def get_city_sales(df):
    return df.groupby('city')['total_amount'].sum()

def get_monthly_sales(df):
    return df.groupby(df['date'].dt.month)['total_amount'].sum()

def get_top_category(df):
    return df.groupby('category')['total_amount'].sum().idxmax()

def get_average_sales(df):
    return np.mean(df['total_amount'])