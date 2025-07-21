# Delta Team: Paul Fralix, Sylvester Brandon, Reed Bennell, Tyler Freese
# Milestone #3 Bacchus Winery - Employee Hours Worked in Last 4 Quarters- 07/20/2025
# This script queries the total hours worked by each employee in the last four quarters and displays it in a tabular format.

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime, timedelta
from tabulate import tabulate  # Install with: pip install tabulate

# --- CONFIGURATION ---
config = {
    "host": "localhost",
    "user": "root",
    "password": "your password here",  # Replace with your actual password
    "database": "bacchus_winery"
}

# --- DISPLAY FUNCTION FOR EMPLOYEE HOURS ---
def show_employee_hours_report(cursor, title):
    print("\n" + "=" * 58)
    print(f" ------ {title} -------")
    print("=" * 58 + "\n")

    # Calculate one year ago
    today = datetime.today()
    one_year_ago = today - timedelta(days=365)

    # Query for total hours worked by each employee in the last 4 quarters
    cursor.execute("""
        SELECT 
            e.EmployeeID,
            CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
            SUM(w.HoursWorked) AS TotalHours
        FROM 
            Employees e
        JOIN 
            Work_Log w ON e.EmployeeID = w.EmployeeID
        WHERE 
            w.WorkDate >= %s
        GROUP BY 
            e.EmployeeID, EmployeeName
        ORDER BY 
            TotalHours DESC;
    """, (one_year_ago.strftime('%Y-%m-%d'),))

    results = cursor.fetchall()

    if results:
        headers = ["Employee ID", "Employee Name", "Total Hours Worked"]
        print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No work log data available for the last four quarters.")

# --- MAIN EXECUTION ---
try:
    db = mysql.connector.connect(**config)
    print(f"\nConnected to database: {config['database']}\n")
    cursor = db.cursor()

    # Show report
    show_employee_hours_report(cursor, "EMPLOYEE HOURS REPORT - LAST 4 QUARTERS")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Database connection error: {err}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nDatabase connection closed.")
