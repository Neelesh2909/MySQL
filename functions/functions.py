'''

    @Author: Neelesh Rawat
    @Date: 18-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 18-04-2022
    @Title : Functions in Mysql

    
'''

import mysql.connector

class Functions:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",passwd="admin@123")
            # creating database_cursor to perform SQL operation
            self.db_cursor = self.con.cursor()
        except Exception as e:
            print(f"Raised Exception : {e}")

    def use_db(self,db_name):
        """
        Description:
            This function is used to determine which database is to be used
        Parameter:
            db_name: The name of the database to be used
        Return:
            None
        """
        self.db_cursor.execute("USE {}".format(db_name))

    def execute_func(self,query):
        """
        Description:
            This function is used to execute the sql query passed
        Parameter:
            query: The sql query which is to be executed
        Return:
            None
        """
        try:
            self.db_cursor.execute(query)
            data = self.db_cursor.fetchall()
            for x in data:
                print(x[0])
        except Exception as e:
            print(f"Raised Exception : {e}")

if __name__ == "__main__":
    func_inst = Functions()

    try:
        print("Welcome to Functions in MySQL using Python")
        # To use a specific database
        func_inst.use_db('db_demo')
        while True:
            query = input("Enter your sql query here : ")
            func_inst.execute_func(query)
            if input("Do you wish to Continue (y/n): ") != 'y':
                break
    except Exception as e:
        print(f"Raised Exception : {e}")


# List of some of the Date Time Functions-->

# It returns the current date
# SELECT CURDATE();
# SELECT CURRENT_DATE();

# It returns the current time
# SELECT CURTIME();
# SELECT CURRENT_TIME();

# It returns the current date and time
# SELECT NOW();
# SELECT SYSDATE();

# It returns the month part for a give date
# SELECT MONTH("2019-04-19");

# It returns the year part for a give date
# SELECT YEAR("2019-04-19");

# It returns the day part for a give date
# SELECT DAY("2019-04-19");

# Add time values (intervals) to a date value
# SELECT ADDDATE('2008-01-02', INTERVAL 45 DAY);

# Add time
# SELECT ADDTIME('01:00:00.999999', '02:00:00.999998');

# Extract the date part of a date or datetime expression
# SELECT DATE('2003-12-31 01:02:03');

# Add time values (intervals) to a date value
# SELECT DATE_ADD('2018-05-01',INTERVAL 1 DAY);

# Subtract a time value (interval) from a date
# SELECT DATE_SUB('2018-05-01',INTERVAL 1 YEAR);

# Subtract two dates
# SELECT DATEDIFF('2007-12-31 23:59:59','2007-12-20');

# Format date as specified
# SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
# SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s');

# Return the name of the weekday
# SELECT DAYNAME('2007-02-03');

# Return the day of the month (0-31)
# SELECT DAYOFMONTH('2007-02-03');

# Return the weekday index of the argument(1 = Sunday, 2 = Monday, …, 7 = Saturday).
# SELECT DAYOFWEEK('2007-02-04');

# Return the day of the year (1-366)
# SELECT DAYOFYEAR('2007-02-03');

# Extract part of a date
# SELECT EXTRACT(YEAR FROM '2019-07-02');
# SELECT EXTRACT(YEAR_MONTH FROM '2019-07-02 01:02:03');

# Extract the hour
# EXTRACT HOUR('10:05:03');

# Return the last day of the month for the argument
# SELECT LAST_DAY('2003-02-05');

# Return the name of the month
# SELECT MONTHNAME('2008-02-03');

# Extract the time portion of the expression passed
# SELECT TIME('2003-12-31 01:02:03');

# Subtract time
# SELECT TIMEDIFF('2000:01:01 00:00:00','2000:01:01 00:00:00.000001');

# Return the calendar week of the date (1-53)
# SELECT WEEKOFYEAR('2008-02-20');

# *******************************************************************************************

# List of some of the Numeric Functions--> 

# It returns the absolute value
# SELECT ABS(-40);
# SELECT ABS(40);

# It returns the square root of the value
# SELECT SQRT(25);

# It returns the remainder 
# SELECT MOD(10,3);

# It returns the a to power of b
# SELECT POWER(2,5);

# It truncates a number to the specified number of decimal places
# SELECT TRUNCATE(40.1234,3);
# SELECT TRUNCATE(40.1234,2);
# SELECT TRUNCATE(6876,-1);
# SELECT TRUNCATE(6876,-2);
# SELECT TRUNCATE(68763456,-5);

# It returns the greatest value in the provided values
# SELECT GREATEST(300,250,500,100,400);

# It returns the least value in the provided values
# SELECT LEAST(300,250,500,100,400);

# Return the smallest integer value not less than the argument
# SELECT CEILING(1.23);
# SELECT CEILING(-1.23);

# Returns the value of e (the base of natural logarithms) raised to the power of X
# SELECT EXP(2);

# Return the largest integer value not greater than the argument
# SELECT FLOOR(1.23);

# Return the natural logarithm of the first argument
# SELECT LOG(2);

# Return the base-10 logarithm of the argument
# SELECT LOG10(2);

# Return the base-2 logarithm of the argument
# SELECT LOG2(65536);

# Return the value of pi
# SELECT PI();

# Return a random floating-point value
# SELECT RAND();

# Return the cosine
# SELECT COS(PI());

# Return the cotangent
# SELECT COT(12);

# Return the sine of the argument
# SELECT SIN(PI());

# Return the tangent of the argument
# SELECT TAN(PI());

# ***********************************************************************************

# List of some of the String Functions--> 


# It will convert all the employee names into UPPER CASE
# SELECT UPPER('smith');
# SELECT UPPER(emp_Name) FROM tbl_employee;

# It will convert all the employee names into LOWER CASE
# SELECT LOWER('SMITH');
# SELECT LOWER(emp_Name) From tbl_employee;

# It will return the length of all the employee names
# SELECT LENGTH('Welcome');
# SELECT LENGTH(emp_Name) FROM tbl_employee;
# SELECT emp_Name from tbl_employee where LENGTH(emp_Name) = 7;

# It will remove the specified characters from both sides
# SELECT TRIM('   Oracle     ');
# SELECT TRIM('z' from 'zzoraclezzzzz');

# It returns the position of character within a string
# SELECT INSTR('Oracle','e');

# It returns the substring of the string
# SELECT SUBSTR('Oracle', 3,3);
# SELECT SUBSTRING(emp_Name,1,3) FROM tbl_employee;

# It joins two strings
# SELECT CONCAT('STRING','LY');

# Return concatenate with separator
# SELECT CONCAT_WS(',','First name','Second name','Last Name');

# Return numeric value of left-most character
# SELECT ASCII('Neelesh');

# Return a string containing binary representation of a number
# SELECT BIN(12);

# Return length of argument in bits
# SELECT BIT_LENGTH('text');

# Return number of characters in argument
# SELECT CHARACTER_LENGTH('NEELESH');

# Hexadecimal representation of decimal or string value
# SELECT HEX('abc');

# Insert substring at specified position up to specified number of characters
# SELECT INSERT('Quadratic', 3, 4, 'What');

# Return the position of the first occurrence of substring
# SELECT LOCATE('bar', 'foobarbar');

# Remove leading spaces
# SELECT LTRIM('  barbar');

# Repeat a string the specified number of times
# SELECT REPEAT('MySQL', 3);

# Replace occurrences of a specified string
# SELECT REPLACE('www.mysql.com', 'w', 'Ww');

# Reverse the characters in a string
# SELECT REVERSE('abc');

# Return the specified rightmost number of characters
# SELECT RIGHT('foobarbar', 4);


# ************************************************************************

# List of some of the Aggregate Functions--> 

# It returns average salaries of employees
# SELECT AVG(emp_salary) FROM tbl_employee;

# It returns sum of all the salaries of employees
# SELECT SUM(emp_salary) FROM tbl_employee;

# It returns minimum salary out of all the salaries of employees
# SELECT MIN(emp_salary) FROM tbl_employee;

# It returns maximum salary out of all the salaries of employees
# SELECT MAX(emp_salary) FROM tbl_employee;

# It returns the count of salary of the employees
# SELECT COUNT(emp_salary) FROM tbl_employee;