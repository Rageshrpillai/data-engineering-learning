SQl basics

1st Hour

# DATABASE

    A database is a container that stores multiple tables.
    Used for storing, managing, and retrieving structured data.

# Tables

A table is like an Excel sheet with rows and columns.
Each table stores one type of information (customers, products, orders).

# Rows

A row is a single complete data entry in a table.
Example: one customer, one order, one product.

# Colums

A column is a single attribute or field in a table.
Examples: name, age, salary, address.

# Primary key

A primary key uniquely identifies each row in a table.

        Must be unique
        Cannot be NULL
        One primary key per table
        Example: id

# fourign key

    A foreign key is a column in one table that refers to the primary key of another table.
    Used to create relationships between tables.
    Example: orders.user_id referencing users.id.

# SELECT Basics

Select all columns:
SELECT \* FROM table;

Select specific columns:
SELECT column1, column2 FROM table;

# WHERE Clause (Filtering Data)

Used to select only rows that match a condition.

Examples:

WHERE age > 18
WHERE city = 'Delhi'
WHERE salary >= 50000

# AND Operator

Combines two conditions — both must be true.

Example:

SELECT \* FROM customers
WHERE age > 18 AND city = 'Delhi';

# ORDER BY (Sorting Results)

Sort results in ascending or descending order.

ORDER BY age; -- ascending
ORDER BY age DESC; -- descending

# IN Operator

Short form of multiple OR conditions.

WHERE city IN ('Delhi', 'Chennai');

Equivalent to:

WHERE city = 'Delhi' OR city = 'Chennai';

# <> Operator (Not Equal To)

WHERE city <> 'Mumbai';

Means: show rows where city is NOT Mumbai.

# LIKE Operator (Pattern Matching)

Used for searching text.

Examples:

name LIKE 'Ra%' -- starts with Ra
name LIKE '%esh' -- ends with esh
name LIKE '%am%' -- contains am

# SQL ORDER

SELECT
FROM
JOIN
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
