'''

    @Author: Neelesh Rawat
    @Date: 21-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 21-04-2022
    @Title : Index in Mysql

    
'''

import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('passwd')

class Index:
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


    def create_index(self,query):
        """
        Description:
            This function is used to create an index
        Parameter:
            query: The sql query which is to be executed
        Return:
            None
        """
        self.db_cursor.execute(query)


    def execute_select(self,query):
        """
        Description:
            This function is used to execute the query passed
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


    def drop_index(self,query):
        """
        Description:
            This function is used to drop the index
        Parameter:
            query: The sql query which is to be executed
        Return:
            None
        """
        self.db_cursor.execute(query)
    

if __name__ == "__main__":
    index_inst = Index()
    try:
        print("Welcome to Index in MySQL using Python")
        index_inst.use_db('db_demo')
        # index_inst.create_index("CREATE INDEX contact_id ON state(FK_country_id)")
        index_inst.execute_select('select * from state where FK_country_id = 1')
        # index_inst.drop_index("DROP INDEX contact_id ON state")
    except Exception as e:
        print(f"Raised Exception : {e}")