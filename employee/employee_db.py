import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="emre99",
    database="companydb"
)
mycursor = mydb.cursor()


class EmployeeDB:
    def __init__(self):
        pass

    def __insert_employee(self,employee_name,employee_type,department_name,department_id):
        try:
            sql = f"INSERT INTO employees (employee_name,employee_type,department_name,department_id) VALUES{employee_name,employee_type, department_name, department_id}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def __delete_employee(self, delete_employee_name):

        try:
            sql = f"DELETE FROM employees WHERE employee_name is '{delete_employee_name}'"

            mycursor.execute(sql)

            mydb.commit()

            print(f"Employee {delete_employee_name} fired successfully")

        except:

            print(f"There is no such employee")

    def __get_manager_name(self, employee_manager_name_check):

        try:

            mycursor.execute(f"SELECT employee_name FROM employees WHERE employee_name is'{employee_manager_name_check}'")

            myresult = mycursor.fetchone()

            print(f"{myresult}")

        except:

            print(f"Manager {employee_manager_name_check} does not exist")

    def __get_employee_name(self, employee_name_check):

        try:

            mycursor.execute(f"SELECT employee_name FROM employees WHERE employee_name  ='{employee_name_check}'")

            myresult = mycursor.fetchone()

            if myresult == None:
                print("No employee with this name")
            else:
                print(f"{myresult}")

        except:

            print(f"Employee {employee_name_check} does not exist")



    def __get_all_employee_names(self):
        sql = "SELECT * FROM employees"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        if myresult == []:
            print("Still no employees hired")
        else:
          for x in myresult:
            print(x)



    def __get_hr_employees(self):

        try:
            mycursor.execute(f"SELECT employee_name FROM employees WHERE employee_type = 'HR'")

            myresult = mycursor.fetchall()

            if myresult == []:
                print("No HR employees registered")
            else:
                for x in myresult:
                  print(x)


        except:

            print(f"HR employees do not exist")


    def __get_developers(self):

        try:
            mycursor.execute(f"SELECT employee_name FROM employees WHERE employee_type = 'Developer'")

            myresult = mycursor.fetchall()

            if myresult == []:
                print("No developer employees registered")
            else:
                for x in myresult:
                    print(x)
        except:

            print(f"Developers do not exist")




    def insert_employee(self,employee_name,employee_type,department_name,department_id):
        return self.__insert_employee(employee_name,employee_type,department_name,department_id)


    def delete_employee(self, delete_employee_name):
        return self.__delete_employee(delete_employee_name)

    def get_manager_name(self, employee_manager_name_check):
        return self.__get_manager_name(employee_manager_name_check)

    def get_employee_name(self, employee_name_check):
        self.__get_employee_name(employee_name_check)

    def get_all_employee_names(self):
        return self.__get_all_employee_names()

    def get_hr_employees(self):
        return self.__get_hr_employees()

    def get_developers(self):
        return self.__get_developers()



