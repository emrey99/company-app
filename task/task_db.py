import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="emre99",
    database="companydb"
)
mycursor = mydb.cursor()

class TaskDB:

    def __init__(self):
        pass

    def __insert_task(self,task_name, task_description , employee_name ,employee_id):
        try:
          sql = f"INSERT INTO tasks (task_name, task_description , employee_name ,employee_id) VALUES{task_name, task_description, employee_name, employee_id}"

          mycursor.execute(sql)

          mydb.commit()

        except:

            mydb.rollback()


    def __delete_task(self,delete_task_name):

        try:
            sql = f"DELETE FROM tasks WHERE company_name = '{delete_task_name}'"

            mycursor.execute(sql)

            mydb.commit()

            print("Task deleted successfully")

        except:

            print(f"There is no such task")


    def __select_employees_with_task(self,task_name):

        try:
            sql = f"SELECT employee_name FROM tasks WHERE task_name = '{task_name}'"

            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            for x in myresult:
               print(x)

        except:
            print("No employees with given task")

    def __select_task_employees(self, employee_name):

        try:
            sql = f"SELECT task_name FROM tasks WHERE employee_name = '{employee_name}'"

            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

        except:
            print("No tasks with given employees")


    def insert_task(self,task_name, task_description , employee_name ,employee_id):
        return self.__insert_task(task_name, task_description , employee_name ,employee_id)

    def delete_task(self,delete_task_name):
        return self.__delete_task(delete_task_name)

    def select_employees_with_task(self,task_name):
        return self.__select_employees_with_task(task_name)

    def select_task_employees(self, employee_name):
        return self.__select_task_employees(employee_name)


