# Why JOIN exists

Databases are normalized: related data is stored in different tables (e.g., customers, orders).

To answer cross-table questions ("who bought what?"), we connect rows across tables using JOINs.

JOIN connects a Primary Key (PK) in one table to a Foreign Key (FK) in another.

# Basic terms

    INNER JOIN (JOIN): returns only rows where matching keys exist in both tables.

    LEFT JOIN (LEFT OUTER JOIN): returns all rows from the left table, with matched rows from the right; right-side columns are NULL when there is no match.

    RIGHT JOIN (RIGHT OUTER JOIN): mirror of LEFT JOIN — all rows from the right table; left columns are NULL when there is no match.

    FULL OUTER JOIN: returns all rows from both tables; non-matches produce NULL on the missing side.

    SELF JOIN: join a table to itself using aliases (useful for hierarchical or pair queries).

# Visual (Venn) intuition

    Use two overlapping circles: left = table A, right = table B

    INNER: shade only the overlap

    LEFT: shade the entire left circle + overlap

    RIGHT: shade the entire right circle + overlap

    FULL: shade both circles fully

# ON vs WHERE — the most important rule

    ON decides how rows are paired (matching logic) during the join stage.

    WHERE filters the joined result after the join stage.

    Consequences:

    Placing a condition on the right table in WHERE after a LEFT JOIN will remove NULLs and can turn the LEFT JOIN into an effective INNER JOIN.

    Use ON for matching conditions that must preserve outer-join behaviour; use WHERE for post-join filters.

    Memory: ON = marriage rule; WHERE = who gets to stay at the party.

# NULL behaviour

    In LEFT JOIN, right-side columns become NULL for unmatched left rows; left-side columns never become NULL because of the join.

    In RIGHT JOIN, left-side columns become NULL for unmatched right rows.

    In FULL JOIN, either side can have NULL for unmatched rows.

    To test missing matches: use IS NULL on the side expected to be NULL (the non-preserved side).
