# Delta Team: Paul Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese
# Revised employee hours.py to show total hours worked per employee over the last 4 quarters
# Milestone # 5 07/27/2025 bacchus_Winery - Employee Hours Report


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

# --- DISPLAY FUNCTION: TOTAL HOURS PER EMPLOYEE ---
def show_total_employee_hours(cursor, title):
    print("\n" + "=" * 75)
    print(f"  -------     {title}    -------")
    print("=" * 75 + "\n")

    now = datetime.now()
    one_year_ago = now - timedelta(days=365)
    print(f"Query executed on: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Query: Total hours worked per employee over last 4 quarters
    query = """
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
    """
    cursor.execute(query, (one_year_ago.strftime('%Y-%m-%d'),))
    results = cursor.fetchall()

    if results:
        headers = ["Employee ID", "Employee Name", "Total Hours Worked (Last 4 Quarters)"]
        print(tabulate(results, headers=headers, tablefmt="fancy_grid", floatfmt=".2f"))
    else:
        print("No work log data available for the last four quarters.")

# --- MAIN EXECUTION ---
try:
    db = mysql.connector.connect(**config)
    print(f"\nConnected to database: {config['database']}\n")
    cursor = db.cursor()

    # Show report
    show_total_employee_hours(cursor, "TOTAL HOURS WORKED PER EMPLOYEE - LAST 4 QUARTERS")

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
