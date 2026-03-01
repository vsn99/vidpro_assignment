PRAGMA foreign_keys = ON;

-- Delete any table if they exist.

DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Customer;

-- Queries to create tables as per ER Diagram.

CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY,
    age INTEGER
);

CREATE TABLE Sales (
    sales_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Items (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    sales_id INTEGER,
    item_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);

-- Customers table records
INSERT INTO Customer VALUES (1,21);
INSERT INTO Customer VALUES (2,23);
INSERT INTO Customer VALUES (3,35);
INSERT INTO Customer VALUES (4,42);

-- Items table records
INSERT INTO Items VALUES (1,'x');
INSERT INTO Items VALUES (2,'y');
INSERT INTO Items VALUES (3,'z');

-- Sales table records
INSERT INTO Sales VALUES (100,1);
INSERT INTO Sales VALUES (101,1);
INSERT INTO Sales VALUES (102,2);
INSERT INTO Sales VALUES (103,3);
INSERT INTO Sales VALUES (104,4);

-- Orders table records.
INSERT INTO Orders VALUES (1,100,1,4);
INSERT INTO Orders VALUES (2,100,2,NULL);
INSERT INTO Orders VALUES (3,100,3,NULL);
INSERT INTO Orders VALUES (4,101,1,6);
INSERT INTO Orders VALUES (5,101,2,NULL);
INSERT INTO Orders VALUES (6,101,3,NULL);
INSERT INTO Orders VALUES (7,102,1,1);
INSERT INTO Orders VALUES (8,102,2,1);
INSERT INTO Orders VALUES (9,102,3,1);
INSERT INTO Orders VALUES (10,103,1,NULL);
INSERT INTO Orders VALUES (11,103,2,NULL);
INSERT INTO Orders VALUES (12,103,3,2);
INSERT INTO Orders VALUES (13,104,1,5);
INSERT INTO Orders VALUES (14,104,2,NULL);
INSERT INTO Orders VALUES (15,104,3,NULL);