# Delta Team: Paul Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese
# Milestone # 5 bacchus_winery-distributor-wine-purchased-query.py
# Bacchus Winery Case Study 07/27/2025
# Script to show which distributors purchased what wine

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
    CONCAT(d.FirstName, ' ', d.LastName) AS DistributorName,
    p.Name AS WineName,
    od.Quantity,
    o.OrderDate
FROM Distributors d
JOIN Orders o ON d.DistributorID = o.DistributorID
JOIN Order_Details od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.Type = 'Wine'
ORDER BY d.LastName, o.OrderDate;
"""

# Fetch and display the results in a DataFrame
df = pd.read_sql(query, conn)

# Display the DataFrame as a nicely formatted table
title = "--- Distributor Wine Purchases ---"
line_width = 61

print("\n" + "=" * line_width)
print(title.center(line_width))
print("=" * line_width + "\n")

print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

# Close the connection
conn.close()
