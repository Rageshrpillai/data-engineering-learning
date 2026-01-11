# GROUP BY Notes

## 1. What GROUP BY Does

GROUP BY groups rows that have the same values into buckets.
After grouping, SQL applies aggregate functions to each bucket.

Example bucket formation:

Delhi → [row1, row3, row5]
Mumbai → [row2]
Chennai → [row4]

## 2. Allowed in SELECT with GROUP BY

SELECT can contain only:

1. Columns used in GROUP BY
2. Aggregate functions (SUM, COUNT, AVG, MIN, MAX)

Example:

```sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city;
```

---

## 3. Common Aggregate Functions

- COUNT() – number of rows
- SUM() – sum of values
- AVG() – average
- MIN() – smallest
- MAX() – largest
- COUNT(DISTINCT col) – unique count

---

## 4. HAVING vs WHERE

- **WHERE** filters rows _before_ grouping.
- **HAVING** filters groups _after_ grouping.

Example (invalid):

```sql
WHERE SUM(amount) > 500   -- aggregate cannot be used in WHERE
```

Correct:

```sql
HAVING SUM(amount) > 500  -- ✔ valid
```

---

## 5. SQL Execution Order

```
FROM
JOIN
WHERE
GROUP BY
HAVING
ORDER BY
```

---

## 6. GROUP BY + ORDER BY

You can order by:

- grouped columns
- aggregate expressions
- column alias

Example:

```sql
SELECT city, COUNT(*) AS total
FROM customers
GROUP BY city
ORDER BY total DESC;
```

---

## 7. GROUP BY with JOIN

Very common in real data engineering tasks.

Example:

```sql
SELECT c.city, SUM(o.amount) AS total_amount
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.city;
```

---
