# Delta Team: Paul Fralix, Sylvester Brandon, Reed Bennell, Tyler Freese
# Milestone #3 Bacchus Winery - Supplier Delivery Report 07/20/2025       
# supplier-delivery-report.py
# Generates a report on supplier deliveries, including delays and item details.

import mysql.connector
import pandas as pd
from tabulate import tabulate  # Install with: pip install tabulate

# --- CONNECT TO DATABASE ---
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your password here',  # Replace with your secure password
        database='bacchus_winery'
    )

    query = """
    SELECT 
        s.Name AS Supplier,
        so.ExpectedArrivalDate,
        so.ActualArrivalDate,
        DATEDIFF(so.ActualArrivalDate, so.ExpectedArrivalDate) AS DaysLate,
        so.Status,
        si.ItemName,
        si.Quantity
    FROM Supply_Orders so
    JOIN Suppliers s ON so.SupplierID = s.SupplierID
    JOIN Supply_Items si ON so.SupplyOrderID = si.SupplyOrderID
    ORDER BY so.OrderDate;
    """

    df = pd.read_sql(query, conn)

    # --- DISPLAY REPORT ---
    title = "SUPPLIER DELIVERY REPORT - ORDER STATUS & DELAYS"
    line_width = 121

    print("\n" + "=" * line_width)
    print(title.center(line_width))
    print("=" * line_width + "\n")


    if not df.empty:
        print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))
    else:
        print("No supplier delivery data available.")

except mysql.connector.Error as err:
    print(f"Database error: {err}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("\nDatabase connection closed.")
