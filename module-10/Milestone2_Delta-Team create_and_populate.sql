# Milestone 2: Create and Populate Tables for Bacchus Winery
# Team: Delta-Team, Members: Paul Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese
-- Drop existing
DROP TABLE IF EXISTS Work_Hours, Employees, Supply_Orders, Suppliers, Order_Details, Orders, Products, Customers;

-- Customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Email VARCHAR(150),
    Phone VARCHAR(20)
);

INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('Alice', 'Smith', 'alice@example.com', '555-1111'),
('Bob', 'Johnson', 'bob@example.com', '555-2222'),
('Carol', 'Lee', 'carol@example.com', '555-3333'),
('David', 'Brown', 'david@example.com', '555-4444'),
('Eva', 'Davis', 'eva@example.com', '555-5555'),
('Frank', 'Wilson', 'frank@example.com', '555-6666');

-- Products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Type VARCHAR(50),
    Price DECIMAL(10,2)
);

INSERT INTO Products (Name, Type, Price) VALUES
('Merlot', 'Wine', 15.50),
('Cabernet', 'Wine', 18.75),
('Chablis', 'Wine', 12.25),
('Chardonnay', 'Wine', 25.00),
('Cheese Platter', 'Food', 10.00),
('Gift Basket', 'Gift', 25.00);

-- Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders (CustomerID, OrderDate, Status) VALUES
(1, '2025-07-01', 'Completed'),
(2, '2025-07-02', 'Pending'),
(3, '2025-07-03', 'Shipped'),
(4, '2025-07-04', 'Completed'),
(5, '2025-07-05', 'Completed'),
(6, '2025-07-06', 'Pending');

-- Order Details
CREATE TABLE Order_Details (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO Order_Details (OrderID, ProductID, Quantity) VALUES
(1, 4, 1),
(2, 2, 3),
(3, 3, 1),
(4, 5, 2),
(5, 6, 1),
(6, 1, 4);

-- Suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    ContactName VARCHAR(100),
    ContactEmail VARCHAR(150),
    City VARCHAR(100)
);

INSERT INTO Suppliers (Name, ContactName, ContactEmail, City) VALUES
('Box and Label Ltd', 'George Green', 'george@boxandlabel.com', 'Napa'),
('Bottling Supplies Ltd', 'Sara White', 'sara@bottlingsupplies.com', 'Sonoma'),
('Vats and Tubing Ltd', 'Tom Black', 'tom@vatsandtubing.com', 'Healdsburg');

-- Supply Orders
CREATE TABLE Supply_Orders (
    SupplyOrderID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierID INT,
    OrderDate DATE,
    ArrivalDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

INSERT INTO Supply_Orders (SupplierID, OrderDate, ArrivalDate, Status) VALUES
(1, '2025-06-20', '2025-06-25', 'Received'),
(2, '2025-06-22', '2025-06-27', 'Received'),
(3, '2025-06-24', '2025-06-30', 'Pending'),
(1, '2025-07-01', NULL, 'Pending'),
(2, '2025-07-02', NULL, 'Ordered'),
(3, '2025-07-03', NULL, 'Ordered');

-- Employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Position VARCHAR(100),
    HourlyRate DECIMAL(10,2)
);

INSERT INTO Employees (FirstName, LastName, Position, HourlyRate) VALUES
('Janet', 'Collins', 'Payroll Manager', 25.00),
('Roz', 'Murphy', 'Marketing Manager', 25.50),
('Bob', 'Ulrich', 'Marketing Assistant', 20.75),
('Henry', 'Doyle', 'Production Manager', 25.25),
('Maria', 'Constanza', 'Distribution Manager', 24.25),
('George', 'Smith', 'Production Worker', 18.00);

-- Work Hours
CREATE TABLE Work_Hours (
    WorkHourID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT,
    WorkDate DATE,
    HoursWorked DECIMAL(5,2),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

INSERT INTO Work_Hours (EmployeeID, WorkDate, HoursWorked) VALUES
(1, '2025-07-01', 8),
(2, '2025-07-01', 7.5),
(3, '2025-07-01', 8),
(4, '2025-07-01', 6),
(5, '2025-07-01', 6),
(6, '2025-07-01', 5);
