-- natural join
SELECT emp_Name from tbl_employee NATURAL JOIN department;

-- inner join
SELECT c.country_name,s.state_name FROM country AS c 
INNER JOIN state AS s
ON c.country_id = s.FK_country_id;

-- left join
SELECT c.country_name,s.state_name FROM country AS c 
LEFT JOIN state AS s
ON c.country_id = s.FK_country_id;

-- right join
SELECT c.country_name,s.state_name FROM country AS c
RIGHT JOIN state AS s
ON c.country_id = s.FK_country_id;

-- self join
SELECT t1.emp_Name AS Employee, t2.emp_Name AS Manager 
FROM tbl_employee AS t1 
INNER JOIN tbl_employee AS t2 
ON t1.manager_id = t2.emp_id;

-- cross join
SELECT e.emp_Name,d.dept_name from tbl_employee e CROSS JOIN department d
WHERE e.emp_id = d.emp_id;