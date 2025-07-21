# Delta Team: Pau Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese
# Milestone #3 Bacchus Winery Case Study - 07/20/2025
# Script to show which customers purchased what wine

import mysql.connector
import pandas as pd
from tabulate import tabulate # Install with: pip install tabulate 

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password here",  # <-- Replace with your actual password
    database="bacchus_winery"   
)

# SQL query to show which customers purchased what wine
query = """
SELECT 
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    p.Name AS WineName,
    od.Quantity,
    o.OrderDate
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN Order_Details od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Type = 'Wine'
ORDER BY c.LastName, o.OrderDate;
"""

# Fetch and display the results in a DataFrame
df = pd.read_sql(query, conn)

# Display the DataFrame as a nicely formatted table
title = "--- Customer Wine Purchases ---"
line_width = 58

print("\n" + "=" * line_width)
print(title.center(line_width))
print("=" * line_width + "\n")

print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

# Close the connection
conn.close()
