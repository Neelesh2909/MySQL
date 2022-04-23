CREATE View vWEmployeesByDepartment
AS
SELECT e.emp_Name, d.dept_name, e.emp_salary, e.emp_contact
FROM tbl_employee AS e
JOIN department AS d
ON e.emp_id = d.emp_id;

SELECT * FROM vWEmployeesByDepartment;


-- view with row level security
CREATE View vWITEmployees
AS
SELECT e.emp_Name, d.dept_name, e.emp_salary, e.emp_contact
FROM tbl_employee AS e
JOIN department AS d
ON e.emp_id = d.emp_id
WHERE d.dept_name = 'IT';

SELECT * FROM vWITEmployees;


-- view with column level security
CREATE View vWNonConfidentialData
AS
SELECT e.emp_Name, d.dept_name
FROM tbl_employee AS e
JOIN department AS d
ON e.emp_id = d.emp_id;

SELECT * from vWNonConfidentialData;