-- groupby_medium_practice.sql

-- 1) Create tables
CREATE TABLE customers (
  id INT,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE orders (
  order_id INT,
  customer_id INT,
  amount INT,
  order_date DATE
);

CREATE TABLE sales (
  sale_id INT,
  product_id INT,
  amount INT,
  sale_date DATE
);

CREATE TABLE employees (
  id INT,
  name VARCHAR(50),
  department VARCHAR(50),
  city VARCHAR(50),
  salary INT,
  hire_date DATE
);

-- 2) Insert sample data
INSERT INTO customers (id, name, city) VALUES
(1, 'Raju', 'Delhi'),
(2, 'Sneha', 'Mumbai'),
(3, 'Arjun', 'Chennai'),
(4, 'Kavya', 'Delhi'),
(5, 'Manoj', NULL);

INSERT INTO orders (order_id, customer_id, amount, order_date) VALUES
(101, 1, 500, '2025-11-01'),
(102, 1, 900, '2025-11-05'),
(103, 3, 250, '2025-10-30'),
(104, 5, 700, '2025-11-03'),
(105, 1, 200, '2025-11-10');

INSERT INTO sales (sale_id, product_id, amount, sale_date) VALUES
(201, 10, 300, '2025-11-01'),
(202, 10, 400, '2025-11-02'),
(203, 20, 1200, '2025-11-03'),
(204, 30, 50, '2025-11-05'),
(205, 10, 200, '2025-11-06'),
(206, 20, 800, '2025-11-07');

INSERT INTO employees (id, name, department, city, salary, hire_date) VALUES
(1, 'Amit', 'Engineering', 'Delhi', 75000, '2022-01-10'),
(2, 'Bina', 'Engineering', 'Delhi', 65000, '2023-05-20'),
(3, 'Chetan', 'Sales', 'Mumbai', 85000, '2021-11-01'),
(4, 'Divya', 'Sales', 'Mumbai', 45000, '2024-02-15'),
(5, 'Esha', 'HR', 'Chennai', 62000, '2020-08-05'),
(6, 'Faisal', 'Engineering', 'Delhi', 90000, '2019-06-01');

-- 3) Practice queries

-- Q1: Total sales per product
-- Query:
SELECT product_id, SUM(amount) AS total_sales
FROM sales
GROUP BY product_id;
-- Expected:
-- product_id=10 total_sales=900
-- product_id=20 total_sales=2000
-- product_id=30 total_sales=50

-- Q2: Orders per customer per month 
SELECT o.customer_id,
       strftime('%Y-%m', o.order_date) AS order_month,
       COUNT(*) AS order_count
FROM orders o
GROUP BY o.customer_id, order_month;
-- Expected (based on sample data):
-- customer 1, 2025-11 -> 3
-- customer 3, 2025-10 -> 1
-- customer 5, 2025-11 -> 1

-- Q3: Departments with more than 2 employees
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
-- Expected: Engineering -> 3

-- Q4: Top-earning department (single row)
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC
LIMIT 1;
-- Expected: Engineering -> 230000

-- Q5: Cities with average salary > 60000
SELECT city, AVG(salary) AS avg_salary
FROM employees
GROUP BY city
HAVING AVG(salary) > 60000;
-- Expected: Delhi (~76666), Mumbai (~65000), Chennai=62000

-- Q6: Most sold product (top 1)
SELECT product_id, COUNT(*) AS sold_count
FROM sales
GROUP BY product_id
ORDER BY sold_count DESC
LIMIT 1;
-- Expected: product_id=10 sold_count=3

-- Q7: Daily revenue for last 30 days 
SELECT sale_date, SUM(amount) AS daily_revenue
FROM sales
WHERE sale_date >= DATE('now','-29 day')
GROUP BY sale_date
ORDER BY sale_date;
-- Expected: sums per sale_date for inserted dates

-- Q8: Customers who spent more than 1000
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
-- Expected: customer_id=1 total_spent=1600


