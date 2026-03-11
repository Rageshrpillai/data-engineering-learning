--.stratascratch

-- EASY QUESTION

Calculates the difference between the highest salaries in the marketing and engineering departments. Output just the absolute difference in salaries.

-- Tables
-- db_employee
-- db_dept

-- Easy
-- ID 10308

--answer
Select  ABS(MAX(CASE WHEN d.department='engineering' THEN e.salary END ) - MAX(CASE WHEN d.department='marketing' THEN e.salary END )) as dif
FROM db_employee e JOIN db_dept d ON e.department_id = d.id

-----------------------------------------------------------------------------------------------------------------------------------


We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.

-- Table
-- ms_employee_salary

-- Easy
-- The difficulty is Easy, because the task requires aggregating data to determine the most recent salary — this involves grouping records by multiple fields to correctly identify individual employees, and then applying an operation to extract the maximum salary value for each group. The logic is not complex but requires understanding of data grouping and applying basic summary operations across different programming language implementations.
-- ID 10299

-- answer
Select id, first_name,last_name, department_id,salary FROM
(Select id, first_name,department_id,last_name,salary, ROW_NUMBER() OVER(PARTITION BY id ORDER BY  SALARY desc  ) as rn FROM ms_employee_salary)t WHERE rn=1 ORDER BY id asc;