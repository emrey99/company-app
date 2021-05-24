import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="emre99",
    database="companydb"
)

mycursor = mydb.cursor()


class DepartmentDB:
    def __init__(self):
        pass

    def __insert_department(self,dep_name,man_name,com_code):

        try:
            sql = f"INSERT INTO departments (dep_name,manager_name,company_code) VALUES {dep_name,man_name,com_code}"

            mycursor.execute(sql)

            mydb.commit()

        except:

            mydb.rollback()

    def __delete_department(self,delete_department_name):

        try:
            sql = f"DELETE FROM departments WHERE company_name = '{delete_department_name}'"

            mycursor.execute(sql)

            mydb.commit()

        except:

            print(f"There is no such department")


    def __get_department_id(self,department_name_check):

        try:
            mycursor.execute(f"SELECT department_id FROM departments WHERE dep_name = '{department_name_check}'")

            myresult = mycursor.fetchone()

            if myresult == None:
                print("There is no department with this name")
            else:
              print(f"{myresult}")

        except:

            print(f"Department {department_name_check} does not exist")


    def insert_department(self,dep_name,man_name,com_code):
        return self.__insert_department(dep_name,man_name,com_code)

    def delete_department(self,delete_department_name):
        return self.__delete_department(delete_department_name)

    def get_department_id(self,department_name_check):
        return self.__get_department_id(department_name_check)


