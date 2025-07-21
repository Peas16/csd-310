# Delta Team: Paul Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese
# Milestone #3 - 07/20/2025
# Bacchus Winery Case Study wine-distribution-sales
# This script connects to a MySQL database and generates a report on wine sales,
# including total sales per wine and identifying wines with no sales.

import mysql.connector
from mysql.connector import errorcode
from decimal import Decimal
from tabulate import tabulate  # Make sure tabulate is installed

# --- CONFIGURATION ---
config = {
    "host": "localhost",
    "user": "root",
    "password": "your password here",  # Replace with your actual MySQL password
    "database": "bacchus_winery"
}

# --- DISPLAY FUNCTION FOR WINE SALES ---
def show_wine_sales_report(cursor, title):
    print(f"\n==== {title} ====\n")

    # Total wine sales
    cursor.execute("""
        SELECT 
            p.Name AS WineName,
            IFNULL(SUM(od.Quantity), 0) AS TotalSold
        FROM Products p
        LEFT JOIN Order_Details od ON p.ProductID = od.ProductID
        WHERE p.Type = 'Wine'
        GROUP BY p.Name
        ORDER BY TotalSold DESC
    """)
    results = cursor.fetchall()

    if results:
        headers = ["Wine Name", "Total Sold"]
        print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No wine sales data found.")

    # Wines with no sales
    cursor.execute("""
        SELECT 
            p.Name AS WineName
        FROM Products p
        LEFT JOIN Order_Details od ON p.ProductID = od.ProductID
        WHERE p.Type = 'Wine'
        GROUP BY p.ProductID
        HAVING SUM(od.Quantity) IS NULL
    """)
    no_sales = cursor.fetchall()

    if no_sales:
        print("\n== Wines with NO Sales ==")
        no_sales_headers = ["Wine Name"]
        print(tabulate(no_sales, headers=no_sales_headers, tablefmt="fancy_grid"))
    else:
        print("\n    All wines have sales.")

# --- MAIN EXECUTION ---
try:
    db = mysql.connector.connect(**config)
    print(f"\nConnected to database: {config['database']}\n")
    cursor = db.cursor()

    # Show report
    show_wine_sales_report(cursor, "WINE SALES REPORT")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Error: {err}")
finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nDatabase connection closed.")
