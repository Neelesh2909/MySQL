'''

    @Author: Neelesh Rawat
    @Date: 18-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 18-04-2022
    @Title : View in Mysql

    
'''

import mysql.connector
import json

with open("D:\MySQL\MySQL\config.json","r") as json_file:
     data = json.load(json_file)

class View:
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

    def select_from_table(self,query):
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

if __name__ == "__main__":
    view_inst = View()
    try:
        print("Welcome to View in MySQL using Python")
        view_inst.use_db('db_demo')
        view_inst.select_from_table('SELECT * FROM vWEmployeesByDepartment;')
    except Exception as e:
        print(f"Raised Exception : {e}")