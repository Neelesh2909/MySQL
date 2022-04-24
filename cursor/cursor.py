'''

    @Author: Neelesh Rawat
    @Date: 21-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 21-04-2022
    @Title : Cursor in Mysql

    
'''

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('passwd')

class Cursor:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=host,user=user,passwd=password)
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


    def execute_procedure(self,query):
        """
        Description:
            This function is used to execute the stored procedure
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


    def drop_procedure(self,query):
        """
        Description:
            This function is used to drop the stored procedure
        Parameter:
            query: The sql query which is to be executed
        Return:
            None
        """
        self.db_cursor.execute(query)
    

if __name__ == "__main__":
    cursor_inst = Cursor()
    try:
        print("Welcome to Cursor in MySQL using Python")
        cursor_inst.use_db('db_demo')
        cursor_inst.execute_procedure('CALL spEmp')
        # cursor_inst.drop_procedure("drop procedure spEmp")
    except Exception as e:
        print(f"Raised Exception : {e}")