1) Create tables
CREATE TABLE customers (
id INT,
name VARCHAR(50),
city VARCHAR(50)
);


CREATE TABLE orders (
order_id INT,
customer_id INT,
amount INT
);


 2) Insert sample data
INSERT INTO customers (id, name, city) VALUES
(1, 'Raju', 'Delhi'),
(2, 'Sneha', 'Mumbai'),
(3, 'Arjun', 'Chennai'),
(4, 'Kavya', 'Delhi'),
(5, 'Manoj', NULL);


INSERT INTO orders (order_id, customer_id, amount) VALUES
(101, 1, 500),
(102, 1, 900),
(103, 3, 250),
(104, 5, 700),
(105, 1, 200);




 3) Practice questions + answers


 Q4: FULL OUTER JOIN (all matches + non-matches)

#Answer:
    SELECT c.name, o.order_id, o.amount
    FROM customers c
    FULL OUTER JOIN orders o ON c.id = o.customer_id
    ORDER BY c.name NULLS LAST, o.order_id;


Alternative (engine with no FULL JOIN support):
SELECT * FROM customers c LEFT JOIN orders o ON c.id=o.customer_id
- UNION



-Q5: List customers who have NO orders (anti-join)
- Answer:
    SELECT c.name
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    WHERE o.customer_id IS NULL;


- Expected rows: Sneha, Kavya


- Q6: List orders that have NO matching customer (orphan orders)
- Answer:
    SELECT o.order_id, o.customer_id, o.amount
    FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.id
    WHERE c.id IS NULL;


- Expected row: 104 (customer_id 5)


- Q7: Show customers who live in Delhi AND have at least one order
- Answer:
    SELECT DISTINCT c.name
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE c.city = 'Delhi';


- Expected rows: Raju


- Q8: Show customers and their orders sorted by amount (DESC)
- Answer :
    SELECT c.name, o.order_id, o.amount
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    ORDER BY o.amount DESC NULLS LAST;


- Expected ordering: 102(900), 104(700), 101(500), 103(250), 105(200), then NULLs


- Q9: JOIN without writing INNER explicitly (JOIN = INNER JOIN)
- Answer:
    SELECT c.name, o.order_id, o.amount
    FROM customers c
    JOIN orders o ON c.id = o.customer_id;


# Q10: Show only the first order (smallest order_id) per customer (no window functions)
 # Answer (subquery approach):
    SELECT c.id AS customer_id, c.name, o.order_id, o.amount
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.order_id = (
    SELECT MIN(o2.order_id) FROM orders o2 WHERE o2.customer_id = c.id
    )
    ORDER BY c.id;


 Expected rows: Raju -> 101 (500), Arjun -> 103 (250), Manoj -> 104 (700)


