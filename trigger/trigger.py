'''

    @Author: Neelesh Rawat
    @Date: 20-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 20-04-2022
    @Title : Trigger in Mysql

    
'''

import os
from unicodedata import name
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('passwd')

class Trigger:
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


    def create_table(self):
        """
        Description:
            This function is used to create a table
        Parameter:
            None
        Return:
            None
        """
        self.db_cursor.execute("create table customers(cust_id int, age int, name varchar(30))")


    def drop_table(self):
        """
        Description:
            This function is used to drop table student
        Parameter:
            None
        Return:
            None
        """
        self.db_cursor.execute("DROP TABLE customers")


    def create_before_insert_trigger(self):
        """
        Description:
            This function is used to create a before insert trigger
        Parameter:
            None
        Return:
            None
        """
        self.db_cursor.execute("""create trigger age_verify before insert on customers for each row if new.age < 0 then set new.age=0; end if;""")


    def insert_into_table(self,values):
        """
        Description:
            This function is used to insert data into table customers
        Parameter:
            values: The values to be inserted into the table students
        Return:
            None
        """
        try:
            student_sql_query = "INSERT INTO customers(cust_id,age,name)VALUES(%s,%s,%s)"
            self.db_cursor.execute(student_sql_query,values)
            self.con.commit()
            print("Record Successfully Inserted")
        except Exception as e:
            print(f"Raised Exception : {e}")


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
    trigger_inst = Trigger()

    def insert_tab():
        cust_id = input("Enter customer id : ")
        age = int(input("Enter customer's age : "))
        name = input("Enter customer's name : ")
        val = (cust_id,age,name)
        trigger_inst.insert_into_table(val)
        
    try:
        print("Welcome to Trigger in MySQL using Python")

        # To use a specific database
        trigger_inst.use_db('triggers')

        # deleting the table
        # trigger_inst.drop_table()

        # creating a customers table within a database
        # trigger_inst.create_table()

        # trigger_inst.create_before_insert_trigger()
        insert_tab()
        trigger_inst.select_from_table("select * from customers")
    except Exception as e:
        print(f"Exception Raised: {e}")

    