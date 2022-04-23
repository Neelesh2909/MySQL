USE demo2;
-- Create a function which returns the cube of a given value.
DELIMITER $$
CREATE FUNCTION Func_Cube(
num INT
)
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE TotalCube INT;
    SET TotalCube = num*num*num;
    RETURN TotalCube;
END	$$
DELIMITER ;

-- Calling a function
SELECT Func_Cube(5);



-- Create a function to calculate the age
DELIMITER $$
CREATE FUNCTION Func_Calculate_Age
(
 Age date
)
RETURNS INT 
DETERMINISTIC
BEGIN
    DECLARE TodayDate DATE;
    SELECT CURRENT_DATE() INTO TodayDate;
    RETURN YEAR(TodayDate) - YEAR(Age);
END$$
DELIMITER ;

-- calling the function
SELECT Func_Calculate_Age('1998-01-29') AS AGE;


-- Real-Time Example of User-Defined Function in MySQL 
-- Create Employee Table
CREATE TABLE Employeeemployee
(
  EmployeeId INT PRIMARY KEY,
  Name VARCHAR(50),
  Salary INT,
  DOB Date
);

-- inserting into employee table
INSERT INTO Employee(EmployeeId, Name, Salary, DOB) VALUES(1001, 'Pranaya', 10000, '1988-02-29');
INSERT INTO Employee(EmployeeId, Name, Salary, DOB) VALUES(1002, 'Anurag', 20000, '1992-06-22');
INSERT INTO Employee(EmployeeId, Name, Salary, DOB) VALUES(1003, 'Sambit', 30000, '1978-04-12');

-- using the user_defined function
SELECT EmployeeId, Name, Salary, DOB, Func_Calculate_Age(DOB) AS Age FROM Employee;

SELECT EmployeeId, Name, Salary, DOB, Func_Calculate_Age(DOB) AS Age 
FROM Employee
WHERE Func_Calculate_Age(DOB) > 30;