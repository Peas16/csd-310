# Delta Team: Paul Fralix, Sylvester Brandon, Reed Bunnell, Tyler Freese
# Milestone # 5 bacchus_winery Case Study
# Date : 2025-07-27
# Revised code to create tables in SQL
# Updated to change Customers table to Distributors and to add more data for Employee Work Log and Finance

DROP TABLE IF EXISTS Work_Log, Finance, Employees, Supply_Items, Supply_Orders, Suppliers, Order_Details, Orders, Products, Distributors;

-- Distributors
CREATE TABLE Distributors (
    DistributorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Email VARCHAR(150),
    Phone VARCHAR(20)
);

INSERT INTO Distributors (FirstName, LastName, Email, Phone) VALUES
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
    Price DECIMAL(10,2),
    InventoryCount INT
);

INSERT INTO Products (Name, Type, Price, InventoryCount) VALUES
('Merlot', 'Wine', 15.50, 200),
('Cabernet', 'Wine', 18.75, 150),
('Chablis', 'Wine', 12.25, 250),
('Chardonnay', 'Wine', 25.00, 100),
('Cheese Platter', 'Food', 10.00, 300),
('Gift Basket', 'Gift', 25.00, 90);

-- Orders
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    DistributorID INT,
    OrderDate DATE,
    Status VARCHAR(50),
    TrackingInfo VARCHAR(100),
    FOREIGN KEY (DistributorID) REFERENCES Distributors(DistributorID)
);

INSERT INTO Orders (DistributorID, OrderDate, Status, TrackingInfo) VALUES
(1, '2025-07-01', 'Completed', 'TX123'),
(2, '2025-07-02', 'Pending', 'TX124'),
(3, '2025-07-03', 'Shipped', 'TX125'),
(4, '2025-07-04', 'Completed', 'TX126'),
(5, '2025-07-05', 'Completed', 'TX127'),
(6, '2025-07-06', 'Pending', 'TX128');

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
    ExpectedArrivalDate DATE,
    ActualArrivalDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);

INSERT INTO Supply_Orders (SupplierID, OrderDate, ExpectedArrivalDate, ActualArrivalDate, Status) VALUES
(1, '2025-06-20', '2025-06-25', '2025-06-27', 'Received'),
(2, '2025-06-22', '2025-06-27', '2025-06-28', 'Received'),
(3, '2025-06-24', '2025-06-30', '2025-07-01', 'Received'),
(1, '2025-07-01', '2025-07-08', NULL, 'Pending'),
(2, '2025-07-02', '2025-07-07', NULL, 'Ordered'),
(3, '2025-07-03', '2025-07-09', NULL, 'Ordered');

-- Supply Items
CREATE TABLE Supply_Items (
    SupplyItemID INT AUTO_INCREMENT PRIMARY KEY,
    SupplyOrderID INT,
    ItemName VARCHAR(100),
    Quantity INT,
    FOREIGN KEY (SupplyOrderID) REFERENCES Supply_Orders(SupplyOrderID)
);

INSERT INTO Supply_Items (SupplyOrderID, ItemName, Quantity) VALUES
(1, 'Bottles', 500),
(2, 'Labels', 300),
(3, 'Vats', 5),
(4, 'Boxes', 400),
(5, 'Tubing', 100),
(6, 'Seals', 600);

-- Employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Position VARCHAR(100),
    Email VARCHAR(150),
    Phone VARCHAR(20),
    HourlyRate DECIMAL(10,2)
);

INSERT INTO Employees (FirstName, LastName, Position, Email, Phone, HourlyRate) VALUES
('Janet', 'Collins', 'Payroll Manager', 'janet@company.com', '555-1001', 25.00),
('Roz', 'Murphy', 'Marketing Manager', 'roz@company.com', '555-1002', 25.50),
('Bob', 'Ulrich', 'Marketing Assistant', 'bob@company.com', '555-1003', 20.75),
('Henry', 'Doyle', 'Production Manager', 'henry@company.com', '555-1004', 25.25),
('Maria', 'Constanza', 'Distribution Manager', 'maria@company.com', '555-1005', 24.25),
('George', 'Smith', 'Production Worker', 'george@company.com', '555-1006', 18.00);

-- Work Log
CREATE TABLE Work_Log (
    WorkLogID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT,
    WorkDate DATE,
    HoursWorked DECIMAL(5,2),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

INSERT INTO Work_Log (EmployeeID, WorkDate, HoursWorked) VALUES

-- Q4 2024 (Oct–Dec)
(1, '2024-10-10', 30), (1, '2024-11-10', 35), (1, '2024-12-10', 40),
(2, '2024-10-10', 38), (2, '2024-11-10', 38), (2, '2024-12-10', 37),
(3, '2024-10-11', 36.5), (3, '2024-11-11', 37), (3, '2024-12-11', 37),
(4, '2024-10-12', 48), (4, '2024-11-12', 48), (4, '2024-12-12', 48),
(5, '2024-10-13', 56), (5, '2024-11-13', 56.5), (5, '2024-12-13', 57),
(6, '2024-10-14', 65), (6, '2024-11-14', 66), (6, '2024-12-14', 65.5),

-- Q1 2025 (Jan–Mar)
(1, '2025-01-10', 37), (1, '2025-02-10', 38), (1, '2025-03-10', 37.5),
(2, '2025-01-11', 37.5), (2, '2025-02-11', 37), (2, '2025-03-11', 38),
(3, '2025-01-12', 36), (3, '2025-02-12', 36.5), (3, '2025-03-12', 37),
(4, '2025-01-13', 48), (4, '2025-02-13', 48), (4, '2025-03-13', 47.5),
(5, '2025-01-14', 56), (5, '2025-02-14', 55.5), (5, '2025-03-14', 56),
(6, '2025-01-15', 65), (6, '2025-02-15', 65.5), (6, '2025-03-15', 65),

-- Q2 2025 (Apr–Jun)
(1, '2025-04-10', 38), (1, '2025-05-10', 37), (1, '2025-06-10', 38),
(2, '2025-04-11', 37.5), (2, '2025-05-11', 37), (2, '2025-06-11',37.5),
(3, '2025-04-12', 36), (3, '2025-05-12', 36.5), (3, '2025-06-12', 36),
(4, '2025-04-13', 48), (4, '2025-05-13', 47.5), (4, '2025-06-13', 48),
(5, '2025-04-14', 56), (5, '2025-05-14', 56), (5, '2025-06-14', 56.5),
(6, '2025-04-15', 65.5), (6, '2025-05-15', 65), (6, '2025-06-15', 65.5),

-- Q3 2025 (Jul–Sep, some already exists — add more)
(1, '2025-07-15', 38),
(2, '2025-07-15', 37.5),
(3, '2025-07-15', 38),
(4, '2025-07-15', 46),
(5, '2025-07-15', 56),
(6, '2025-07-15', 65);

-- Finance
CREATE TABLE Finance (
    FinanceID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT,
    Description VARCHAR(255),
    Amount DECIMAL(10,2),
    EntryDate DATE,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

INSERT INTO Finance (EmployeeID, Description, Amount, EntryDate) VALUES
(1, 'Payroll - Janet Collins', 200.00, '2025-07-01'),
(2, 'Payroll - Roz Murphy', 191.25, '2025-07-01'),
(3, 'Payroll - Bob Ulrich', 166.00, '2025-07-01'),
(4, 'Payroll - Henry Doyle', 151.50, '2025-07-01'),
(5, 'Payroll - Maria Constanza', 145.50, '2025-07-01'),
(6, 'Payroll - George Smith', 90.00, '2025-07-01');
