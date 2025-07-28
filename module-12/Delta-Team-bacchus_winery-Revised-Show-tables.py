# Delta Team: Paul Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese
# Revised Show Tables.py to reflect change in Customer table to Distributor table
# Milestone # 5 bacchus_winery 07/27/2025

import mysql.connector
from mysql.connector import errorcode
from decimal import Decimal
import datetime
from tabulate import tabulate

# Replace with your database credentials
config = {
    "host": "localhost",
    "user": "root",
    "password": "your password here",  # Replace with your actual password
    "database": "bacchus_winery"
}

# --- CLEANER FUNCTION ---
def clean_row(row):
    new_row = []
    for item in row:
        if isinstance(item, (Decimal, float)):  # Format all decimal/float as currency-style
            new_row.append(f"{item:.2f}")
        elif isinstance(item, datetime.date):
            new_row.append(item.strftime('%Y-%m-%d'))
        else:
            new_row.append(item)
    return new_row

# --- GENERIC DISPLAY FUNCTION ---
def show_table(cursor, title, query, headers):
    cursor.execute(query)
    rows = [clean_row(row) for row in cursor.fetchall()]
    print(f"\n-- {title} --")
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

# --- MAIN EXECUTION ---
try:
    db = mysql.connector.connect(**config)
    print(f"\nDatabase user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

    input("\nPress ENTER to continue...")

    cursor = db.cursor()

    # Show Distributors
    show_table(cursor, "DISTRIBUTORS", 
        "SELECT DistributorID, FirstName, LastName, Email, Phone FROM Distributors",
        ["ID", "First Name", "Last Name", "Email", "Phone"])

    # Show Products with Price formatted to 2 decimal places
    show_table(cursor, "PRODUCTS", 
        "SELECT ProductID, Name, Type, Price, InventoryCount FROM Products",
        ["ID", "Name", "Type", "Price", "Inventory"])

    # Show Orders
    show_table(cursor, "ORDERS", 
        """
        SELECT Orders.OrderID, Distributors.FirstName, Distributors.LastName, Orders.OrderDate, Orders.Status
        FROM Orders
        INNER JOIN Distributors ON Orders.DistributorID = Distributors.DistributorID
        ORDER BY Orders.OrderID
        """,
        ["Order ID", "First Name", "Last Name", "Order Date", "Status"])

    # Show Order Details
    show_table(cursor, "ORDER DETAILS", 
        """
        SELECT Order_Details.OrderDetailID, Orders.OrderID, Products.Name, Order_Details.Quantity
        FROM Order_Details
        INNER JOIN Orders ON Order_Details.OrderID = Orders.OrderID
        INNER JOIN Products ON Order_Details.ProductID = Products.ProductID
        ORDER BY Order_Details.OrderDetailID
        """,
        ["Detail ID", "Order ID", "Product", "Quantity"])

    # Show Suppliers
    show_table(cursor, "SUPPLIERS", 
        "SELECT SupplierID, Name, ContactName, ContactEmail, City FROM Suppliers",
        ["ID", "Name", "Contact", "Email", "City"])

    # Show Supply Orders
    show_table(cursor, "SUPPLY ORDERS", 
        """
        SELECT Supply_Orders.SupplyOrderID, Suppliers.Name, Supply_Orders.OrderDate,
               Supply_Orders.ExpectedArrivalDate, Supply_Orders.ActualArrivalDate, Supply_Orders.Status
        FROM Supply_Orders
        INNER JOIN Suppliers ON Supply_Orders.SupplierID = Suppliers.SupplierID
        ORDER BY Supply_Orders.SupplyOrderID
        """,
        ["Supply Order ID", "Supplier", "Order Date", "Expected", "Actual", "Status"])

    # Show Supply Items
    show_table(cursor, "SUPPLY ITEMS", 
        """
        SELECT Supply_Items.SupplyItemID, Supply_Orders.SupplyOrderID, Supply_Items.ItemName, Supply_Items.Quantity
        FROM Supply_Items
        INNER JOIN Supply_Orders ON Supply_Items.SupplyOrderID = Supply_Orders.SupplyOrderID
        ORDER BY Supply_Items.SupplyItemID
        """,
        ["Item ID", "Supply Order ID", "Item Name", "Quantity"])

    # Show Employees with pay rate formatted
    show_table(cursor, "EMPLOYEES", 
        "SELECT EmployeeID, FirstName, LastName, Position, Email, Phone, HourlyRate FROM Employees",
        ["ID", "First Name", "Last Name", "Position", "Email", "Phone", "Rate"])

    # Show Work Logs with Quarter info
    show_table(cursor, "WORK LOG BY QUARTER", 
        """
        SELECT 
            Work_Log.WorkLogID,
            Employees.FirstName,
            Employees.LastName,
            Work_Log.WorkDate,
            Work_Log.HoursWorked,
            CONCAT('Q', QUARTER(Work_Log.WorkDate), ' ', YEAR(Work_Log.WorkDate)) AS QuarterYear
        FROM Work_Log
        INNER JOIN Employees ON Work_Log.EmployeeID = Employees.EmployeeID
        ORDER BY Work_Log.WorkDate
        """,
        ["WorkLog ID", "First Name", "Last Name", "Date", "Hours", "Quarter"])

    # Show Finance entries with amount formatted
    show_table(cursor, "FINANCE", 
        """
        SELECT Finance.FinanceID, Employees.FirstName, Employees.LastName, Finance.Description, Finance.Amount, Finance.EntryDate
        FROM Finance
        INNER JOIN Employees ON Finance.EmployeeID = Employees.EmployeeID
        ORDER BY Finance.FinanceID
        """,
        ["Finance ID", "First Name", "Last Name", "Description", "Amount", "Date"])

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(f"Error: {err}")
finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nDatabase connection closed.")
