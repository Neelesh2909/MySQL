'''

    @Author: Neelesh Rawat
    @Date: 14-04-2022   
    @Last Modified by: Neelesh Rawat
    @Last Modified time: 14-04-2022
    @Title : Crud Operation in Mysql

    
'''
import mysql.connector

class Crud:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",passwd="admin@123")
            # creating database_cursor to perform SQL operation
            self.db_cursor = self.con.cursor()
        except Exception as e:
            print(f"Raised Exception : {e}")
        
# Database operations ---------->

    def create_db(self,db_name):
        """
        Description:
            This function is used to create a database
        Parameter:
            db_name: The name for the database which is to be created
        Return:
            None
        """ 
        lst_db = self.show_db()
        if db_name in lst_db:
            print(f"Database '{db_name}' Already Exists")
        else:
        # executing cursor with execute method and pass SQL query
            self.db_cursor.execute("CREATE DATABASE {}".format(db_name))
            print(f"Database '{db_name}' successfully created..!")


    def show_db(self):
        """
        Description:
            This function is used to show the list of databases
        Parameter:
            None
        Return:
            None
        """
        # get list of all databases
        self.db_cursor.execute("SHOW DATABASES")
        #print all databases
        lst_db = []
        for db in self.db_cursor:
            lst_db.append(db[0])
        # print(lst_db)
        return lst_db


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

    
    def drop_db(self,db_name):
        """
        Description:
            This function is used to drop an existing database
        Parameter:
            db_name: The name of the database to be dropped
        Return:
            None
        """
        lst_db = self.show_db()
        if db_name in lst_db:
            self.db_cursor.execute("DROP DATABASE {}".format(db_name))
            print(f"Database '{db_name}' successfully dropped..!")
        else:
            print(f"No database named '{db_name}' exists..!'")

# Table operations------->

    def create_table(self):
        """
        Description:
            This function is used to create a table
        Parameter:
            None
        Return:
            None
        """
        self.db_cursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT(2), class varchar(50))")

    
    def show_table(self):
        """
        Description:
            This function is used to show the list of tables present in the database in use 
        Parameter:
            None
        Return:
            None
        """
        self.db_cursor.execute("SHOW TABLES")
        #print all tables
        lst_tab = []
        for table in self.db_cursor:
            lst_tab.append(table)
        # print(lst_tab)
        return lst_tab

    
    def alter_table(self):
        """
        Description:
            This function is used to alter table student 
        Parameter:
            None
        Return:
            None
        """
        #Here we modify existing column id
        self.db_cursor.execute("ALTER TABLE student MODIFY age INT(6)")


    def drop_table(self):
        """
        Description:
            This function is used to drop table student
        Parameter:
            None
        Return:
            None
        """
        self.db_cursor.execute("DROP TABLE student")

    # inserting values into the table
    def insert_into_table(self,values):
        """
        Description:
            This function is used to insert data into table student
        Parameter:
            values: The values to be inserted into the table student
        Return:
            None
        """
        try:
            student_sql_query = "INSERT INTO student(name,age,class)VALUES(%s,%s,%s)"
            self.db_cursor.execute(student_sql_query,values)
            self.con.commit()
            print("Record Successfully Inserted")
        except Exception as e:
            print(f"Raised Exception : {e}")


    #read operations
    def select_from_table(self):
        """
        Description:
            This function is used to display student's table data
        Parameter:
            None
        Return:
            None
        """
        try:
            self.db_cursor.execute('select * from student')
            data = self.db_cursor.fetchall()
            for x in data:
                print(x)
        except Exception as e:
            print(f"Raised Exception : {e}")

    # update operations
    def update_tbl(self,name):
        """
        Description:
            This function is used to update student's table 
        Parameter:
            name: The name of student which is to be updated
        Return:
            None
        """
        sql_query = "select * from student where name=%s"
        val = (name,)
        try:
            self.db_cursor.execute(sql_query,val)
            data = self.db_cursor.fetchall()
            for x in data:
                name = x[1]
                age = x[2]
                cls = x[3]
            choice = int(input(f"1.Update your age\n2.Update your class\nEnter your choice : "))
            if choice == 1:
                age = input("Enter age : ")
            elif choice ==2:
                cls = input("Enter class : ")
            else:
                print("Invalid Input")

            sql_query2 = "Update student set age=%s,class=%s where name=%s"
            value = (age,cls,name)
            try:
                self.db_cursor.execute(sql_query2,value)
                self.con.commit()
                print("Record updated successfully..!")
            except Exception as e:
                print(f"Raised Exception : {e}")
        except Exception as e:
            print(f"Raised Exception : {e}")
    
    # delete operations
    def delete_tbl(self,name):
        """
        Description:
            This function is used to delete an existing table
        Parameter:
            name: The name of student based on which the data is to be deleted
        Return:
            None
        """
        query = "delete from student where name=%s"
        try:
            self.db_cursor.execute(query,name)
            self.con.commit()
            print(f"Record Successfully deleted")
        except Exception as e:
            print(f"Raised Exception : {e}")


    def not_valid(self):
        """
        Description:
            This function display a message is the user chooses invalid option
        Parameter:
            None
        Return:
            None
        """
        print("Please choose a correct option from the list mentioned above")


if __name__ == "__main__":
    crud_inst = Crud()

    def insert_tab():
        name = input("Enter student's name : ")
        age = int(input("Enter student's age : "))
        std_class = input("Enter student's class : ")
        val = (name,age,std_class)
        crud_inst.insert_into_table(val)


    def delete_tab():
        name = input("Enter the student's name that you want to delete : ")
        val = (name,)
        crud_inst.delete_tbl(val)
        

    def update_tab():
        name = input("Enter the student's name that you want to update : ")
        crud_inst.update_tbl(name)

        
    try:
        print("Welcome to CRUD Operation in MySQL using Python")

        # showing a list of existing databases
        # lst_db = crud_inst.show_db()
        # print(lst_db)

        # creating a new database
        # crud_inst.create_db('demo3')

        # To use a specific database
        crud_inst.use_db('db_demo')

        # To delete/drop a database
        # crud_inst.drop_db('demo3')

        # creating a student table within a database
        # crud_inst.create_table()

        #  altering the table
        # crud_inst.alter_table()

        # deleting the table
        # crud_inst.drop_table()

        # showing up the list of existing tables
        # lst_tab = crud_inst.show_table()
        # print(lst_tab)

        while True:
            print("Select an option\n1.Insert\n2.Read\n3.Update\n4.Delete")
            choice = int(input("Enter your choice : "))
            switcher = {
                        1: insert_tab,
                        2: crud_inst.select_from_table,
                        3: update_tab,
                        4: delete_tab
                    }
            output = switcher.get(choice,crud_inst.not_valid)()
            if input("Do you wish to Continue (y/n): ") != 'y':
                break
    except Exception as e:
        print(f"Exception Raised: {e}")