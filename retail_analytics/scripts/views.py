from scripts.analysis import *

def show_total_sales(df):
    print(f"\n Total Sales: {get_total_sales(df)}")

def show_top_product(df):
    print(f"\n Top Product: {get_top_product(df)}")

def show_city_sales(df):
    print("\n City-wise Sales:")
    print(get_city_sales(df))

def show_monthly_sales(df):
    print("\n Monthly Sales:")
    print(get_monthly_sales(df))

def show_top_category(df):
    print(f"\n Top Category: {get_top_category(df)}")

def show_average_sales(df):
    print(f"\n Average Sales: {get_average_sales(df)}")