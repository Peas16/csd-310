# Milestone 2: Show Tables for Bacchus Winery   
# Team: Delta-Team, Members: Paul Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese

import mysql.connector
from mysql.connector import errorcode
from decimal import Decimal
import datetime

# Replace with your database credentials
config = {
    "host": "localhost",
    "user": "root",
    "password": "your_password_here",
    "database": "bacchus_winery"
    }

# --- CLEANER FUNCTION ---
def clean_row(row):
    new_row = []
    for item in row:
        if isinstance(item, Decimal):
            new_row.append(f"{item: .2f}")
        elif isinstance(item, datetime.date):
            new_row.append(item.strftime('%Y-%m-%d'))
        else:
            new_row.append(item)
    return tuple(new_row)

def show_customers(cursor, title):
    cursor.execute("""
        SELECT CustomerID, FirstName, LastName, Email, Phone FROM Customers
    """)
    customers = cursor.fetchall()
    print("\n -- {} --".format(title))
    for c in customers:
        print(f"ID: {c[0]}\nName: {c[1]} {c[2]}\nEmail: {c[3]}\nPhone: {c[4]}\n")

def show_products(cursor, title):
    cursor.execute("""
        SELECT ProductID, Name, Type, Price FROM Products
    """)
    products = cursor.fetchall()
    print("\n -- {} --".format(title))
    for p in products:
        print(f"ID: {p[0]}\nName: {p[1]}\nType: {p[2]}\nPrice: ${p[3]:.2f}\n")

def show_orders(cursor, title):
    cursor.execute("""
        SELECT 
            Orders.OrderID, 
            Customers.FirstName, Customers.LastName,
            Orders.OrderDate, Orders.Status
        FROM Orders
            INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
        ORDER BY Orders.OrderID
    """)
    orders = cursor.fetchall()
    print("\n -- {} --".format(title))
    for o in orders:
        print(f"OrderID: {o[0]}\nCustomer: {o[1]} {o[2]}\nDate: {o[3]}\nStatus: {o[4]}\n")

def show_order_details(cursor, title):
    cursor.execute("""
        SELECT 
            Order_Details.OrderDetailID,
            Orders.OrderID,
            Products.Name,
            Order_Details.Quantity
        FROM Order_Details
            INNER JOIN Orders ON Order_Details.OrderID = Orders.OrderID
            INNER JOIN Products ON Order_Details.ProductID = Products.ProductID
        ORDER BY Order_Details.OrderDetailID
    """)
    details = cursor.fetchall()
    print("\n -- {} --".format(title))
    for d in details:
        print(f"DetailID: {d[0]}\nOrderID: {d[1]}\nProduct: {d[2]}\nQuantity: {d[3]}\n")

def show_suppliers(cursor, title):
    cursor.execute("""
        SELECT SupplierID, Name, ContactName, ContactEmail, City FROM Suppliers
    """)
    suppliers = cursor.fetchall()
    print("\n -- {} --".format(title))
    for s in suppliers:
        print(f"ID: {s[0]}\nName: {s[1]}\nContact: {s[2]}\nEmail: {s[3]}\nCity: {s[4]}\n")

def show_supply_orders(cursor, title):
    cursor.execute("""
        SELECT 
            Supply_Orders.SupplyOrderID,
            Suppliers.Name,
            Supply_Orders.OrderDate,
            Supply_Orders.ArrivalDate,
            Supply_Orders.Status
        FROM Supply_Orders
            INNER JOIN Suppliers ON Supply_Orders.SupplierID = Suppliers.SupplierID
        ORDER BY Supply_Orders.SupplyOrderID
    """)
    supplies = cursor.fetchall()
    print("\n -- {} --".format(title))
    for s in supplies:
        print(f"SupplyOrderID: {s[0]}\nSupplier: {s[1]}\nOrderDate: {s[2]}\nArrival: {s[3]}\nStatus: {s[4]}\n")

def show_employees(cursor, title):
    cursor.execute("""
        SELECT EmployeeID, FirstName, LastName, Position, HourlyRate FROM Employees
    """)
    employees = cursor.fetchall()
    print("\n -- {} --".format(title))
    for e in employees:
        print(f"ID: {e[0]}\nName: {e[1]} {e[2]}\nPosition: {e[3]}\nRate: ${e[4]:.2f}\n")

def show_work_hours(cursor, title):
    cursor.execute("""
        SELECT 
            Work_Hours.WorkHourID,
            Employees.FirstName,
            Employees.LastName,
            Work_Hours.WorkDate,
            Work_Hours.HoursWorked
        FROM Work_Hours
            INNER JOIN Employees ON Work_Hours.EmployeeID = Employees.EmployeeID
        ORDER BY Work_Hours.WorkHourID
    """)
    hours = cursor.fetchall()
    print("\n -- {} --".format(title))
    for h in hours:
        print(f"WorkHourID: {h[0]}\nEmployee: {h[1]} {h[2]}\nDate: {h[3]}\nHours: {h[4]:.2f}\n")

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    cursor = db.cursor()

    show_customers(cursor, "DISPLAYING CUSTOMERS")
    show_products(cursor, "DISPLAYING PRODUCTS")
    show_orders(cursor, "DISPLAYING ORDERS")
    show_order_details(cursor, "DISPLAYING ORDER DETAILS")
    show_suppliers(cursor, "DISPLAYING SUPPLIERS")
    show_supply_orders(cursor, "DISPLAYING SUPPLY ORDERS")
    show_employees(cursor, "DISPLAYING EMPLOYEES")
    show_work_hours(cursor, "DISPLAYING WORK HOURS")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\n Database connection closed.")
