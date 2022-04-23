'''

    @Author: Neelesh Rawat
    @Date: 20-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 20-04-2022
    @Title : Stored Procedure in Mysql

    
'''

import mysql.connector
import json

with open("D:\MySQL\MySQL\config.json","r") as json_file:
     data = json.load(json_file)

class StoredProc:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=data['host'],user=data['user'],passwd=data['passwd'])
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
    stored_proc_inst = StoredProc()
    try:
        print("Welcome to Stored Procedure in MySQL using Python")
        stored_proc_inst.use_db('db_demo')
        stored_proc_inst.execute_procedure('CALL sp_GetAllStates')
        # stored_proc_inst.drop_procedure("DROP PROCEDURE sp_GetAllStates")
    except Exception as e:
        print(f"Raised Exception : {e}")