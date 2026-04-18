from scripts.data_cleaning import load_data
from scripts.database import connect_db, setup_table, insert_data, sql_city_sales
from scripts import views

def menu():
    print("\n RETAIL ANALYTICS DASHBOARD")
    print("1. Total Sales")
    print("2. Top Product")
    print("3. City-wise Sales (Pandas)")
    print("4. Monthly Sales")
    print("5. Top Category")
    print("6. Average Sales")
    print("7. City-wise Sales (SQL)")
    print("8. Exit")

def main():
    df = load_data()

    conn = connect_db()
    setup_table(conn)
    insert_data(conn, df)

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            views.show_total_sales(df)

        elif choice == '2':
            views.show_top_product(df)

        elif choice == '3':
            views.show_city_sales(df)

        elif choice == '4':
            views.show_monthly_sales(df)

        elif choice == '5':
            views.show_top_category(df)

        elif choice == '6':
            views.show_average_sales(df)

        elif choice == '7':
            print("\n🗄️ SQL City Sales:")
            print(sql_city_sales(conn))

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

    conn.close()

if __name__ == "__main__":
    main()


    