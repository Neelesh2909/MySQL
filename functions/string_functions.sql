USE db_demo;

-- It will convert all the employee names into UPPER CASE
SELECT UPPER('smith');
SELECT UPPER(emp_Name) FROM tbl_employee;

-- It will convert all the employee names into LOWER CASE
SELECT LOWER('SMITH');
SELECT LOWER(emp_Name) From tbl_employee;

-- It will return the length of all the employee names
SELECT LENGTH('Welcome');
SELECT LENGTH(emp_Name) FROM tbl_employee;
SELECT emp_Name from tbl_employee where LENGTH(emp_Name) = 7;

-- It will remove the specified characters from both sides
SELECT TRIM('   Oracle     ');
SELECT TRIM('z' from 'zzoraclezzzzz');

-- It returns the position of character within a string
SELECT INSTR('Oracle','e');

-- It returns the substring of the string
SELECT SUBSTR('Oracle', 3,3);
SELECT SUBSTRING(emp_Name,1,3) FROM tbl_employee;

-- It joins two strings
SELECT CONCAT('STRING','LY');

-- 	Return concatenate with separator
SELECT CONCAT_WS(',','First name','Second name','Last Name');

-- 	Return numeric value of left-most character
SELECT ASCII('Neelesh');

-- Return a string containing binary representation of a number
SELECT BIN(12);

-- Return length of argument in bits
SELECT BIT_LENGTH('text');

-- 	Return number of characters in argument
SELECT CHARACTER_LENGTH('NEELESH');

-- 	Hexadecimal representation of decimal or string value
SELECT HEX('abc');

-- 	Insert substring at specified position up to specified number of characters
SELECT INSERT('Quadratic', 3, 4, 'What');

-- 	Return the position of the first occurrence of substring
SELECT LOCATE('bar', 'foobarbar');

-- 	Remove leading spaces
SELECT LTRIM('  barbar');

-- Repeat a string the specified number of times
SELECT REPEAT('MySQL', 3);

-- Replace occurrences of a specified string
SELECT REPLACE('www.mysql.com', 'w', 'Ww');

-- 	Reverse the characters in a string
SELECT REVERSE('abc');

-- 	Return the specified rightmost number of characters
SELECT RIGHT('foobarbar', 4);


