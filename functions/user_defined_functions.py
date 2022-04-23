'''

    @Author: Neelesh Rawat
    @Date: 20-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 20-04-2022
    @Title : User Defined Functions in Mysql

    
'''

import mysql.connector

class UserDefinedFunc:
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


    def execute_function(self,query):
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
                print(x)
        except Exception as e:
            print(f"Raised Exception : {e}")

    def drop_function(self,query):
        """
        Description:
            This function is used to drop a existing function
        Parameter:
            query: The sql query which is to be executed
        Return:
            None
        """
        self.db_cursor.execute(query)

if __name__ == "__main__":
    user_func_inst = UserDefinedFunc()
    try:
        print("Welcome to User Defined function in MySQL using Python")
        user_func_inst.use_db('demo2')
        query = "SELECT Func_Cube(5);"
        # query = "SELECT Func_Calculate_Age('1998-01-29') AS AGE;"
        # query = "SELECT EmployeeId, Name, Salary, DOB, Func_Calculate_Age(DOB) AS Age FROM Employee;"
        user_func_inst.execute_function(query)
    except Exception as e:
        print(f"Raised Exception : {e}")