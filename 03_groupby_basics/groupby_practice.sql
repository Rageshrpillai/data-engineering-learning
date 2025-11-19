 Sample Schema for Practice

### customers

```
id | name  | city
1  | Raju  | Delhi
2  | Sneha | Mumbai
3  | Arjun | Chennai
4  | Kavya | Delhi
5  | Manoj | NULL
```

### orders

```
order_id | customer_id | amount | order_date
101      | 1           | 500    | 2025-11-01
102      | 1           | 900    | 2025-11-05
103      | 3           | 250    | 2025-10-30
104      | 5           | 700    | 2025-11-03
105      | 1           | 200    | 2025-11-10
```

### sales

```
sale_id | product_id | amount | sale_date
201     | 10         | 300    | 2025-11-01
202     | 10         | 400    | 2025-11-02
203     | 20         | 1200   | 2025-11-03
204     | 30         | 50     | 2025-11-05
205     | 10         | 200    | 2025-11-06
206     | 20         | 800    | 2025-11-07
```

### employees

```
id | name   | department   | city    | salary | hire_date
1  | Amit   | Engineering  | Delhi   | 75000  | 2022-01-10
2  | Bina   | Engineering  | Delhi   | 65000  | 2023-05-20
3  | Chetan | Sales        | Mumbai  | 85000  | 2021-11-01
4  | Divya  | Sales        | Mumbai  | 45000  | 2024-02-15
5  | Esha   | HR           | Chennai | 62000  | 2020-08-05
6  | Faisal | Engineering  | Delhi   | 90000  | 2019-06-01
```

---

# Medium-Level GROUP BY Practice Questions

These match industry and LeetCode difficulty.

---

## Q1. Total sales per product

```sql
SELECT product_id, SUM(amount) AS total_sales
FROM sales
GROUP BY product_id;
```

---

## Q2. Orders per customer per month

```sql
SELECT customer_id,
       strftime('%Y-%m', order_date) AS order_month,
       COUNT(*) AS order_count
FROM orders
GROUP BY customer_id, order_month;
```

---

## Q3. Departments with more than 2 employees

```sql
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
```

---

## Q4. Top-earning department

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC
LIMIT 1;
```

---

## Q5. Cities with average salary > 60000

```sql
SELECT city, AVG(salary) AS avg_salary
FROM employees
GROUP BY city
HAVING AVG(salary) > 60000;
```

---

## Q6. Most sold product (highest order count)

```sql
SELECT product_id, COUNT(*) AS sold_count
FROM sales
GROUP BY product_id
ORDER BY sold_count DESC
LIMIT 1;
```

---

## Q7. Daily revenue (last 30 days)

```sql
SELECT sale_date, SUM(amount) AS daily_revenue
FROM sales
WHERE sale_date >= DATE('now','-29 day')
GROUP BY sale_date
ORDER BY sale_date;
```

---

## Q8. Customers who spent more than 1000

```sql
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 1000;
```

