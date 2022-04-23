'''

    @Author: Neelesh Rawat
    @Date: 18-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 18-04-2022
    @Title : Joins in Mysql

    
'''
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('passwd')

class Joins:
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
    

    def not_valid(self):
        """
        Description:
            This function display a message based on the choice of the user if it is invalid
        Parameter:
            None
        Return:
            None
        """
        print("Please choose a correct option from the list mentioned above")


if __name__ == "__main__":
    joins_inst = Joins()

    def print_table():
        print("Country Table")
        print()
        joins_inst.select_from_table('Select * from country')
        print('*****************************')
        print("State Table")
        print()
        joins_inst.select_from_table('Select * from state')
        print('*****************************')

    def natural_join_func():
        print("Employee Table")
        print()
        joins_inst.select_from_table('Select * from tbl_employee')
        print('*****************************')
        print("Department Table")
        print()
        joins_inst.select_from_table('Select * from department')
        print('*****************************')
        query = 'SELECT emp_Name from tbl_employee NATURAL JOIN department'
        joins_inst.select_from_table(query)

    def inner_join_func():
        print_table()
        query = 'SELECT c.country_name,s.state_name FROM country AS c INNER JOIN state AS s ON c.country_id = s.FK_country_id'
        joins_inst.select_from_table(query)

    def left_join_func():
        print_table()
        query = 'SELECT c.country_name,s.state_name FROM country AS c LEFT JOIN state AS s ON c.country_id = s.FK_country_id'
        joins_inst.select_from_table(query)

    def right_join_func():
        print_table()
        query = 'SELECT c.country_name,s.state_name FROM country AS c RIGHT JOIN state AS s ON c.country_id = s.FK_country_id'
        joins_inst.select_from_table(query)

    def self_join_func():
        print("Employee Table")
        print()
        joins_inst.select_from_table('Select * from tbl_employee')
        print('*****************************')
        query = 'SELECT t1.emp_Name AS Employee, t2.emp_Name AS Manager FROM tbl_employee AS t1 INNER JOIN tbl_employee AS t2 ON t1.manager_id = t2.emp_id'
        joins_inst.select_from_table(query)

    try:
        print("Welcome to Joins in MySQL using Python")
        # To use a specific database
        joins_inst.use_db('db_demo')
        while True:
            print("Select an option\n1.Natural Join\n2.Inner Join\n3.Left Join\n4.Right Join\n5.Self Join")
            choice = int(input("Enter your choice : "))
            switcher = {
                        1: natural_join_func,
                        2: inner_join_func,
                        3: left_join_func,
                        4: right_join_func,
                        5: self_join_func
                    }
            output = switcher.get(choice,joins_inst.not_valid)()
            if input("Do you wish to Continue (y/n): ") != 'y':
                break
    except Exception as e:
        print(f"Raised Exception : {e}")