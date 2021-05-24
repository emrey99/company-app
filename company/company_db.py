import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="emre99",
    database="companydb"
)
mycursor = mydb.cursor()

class CompanyDB:


    def __insert_company(self,i_company_name,budget,class_type):

        try:

          sql = f"INSERT INTO companies (company_name,budget,class_type) VALUES{i_company_name,budget,class_type}"

          mycursor.execute(sql)

          mydb.commit()


        except:

            mydb.rollback()

    def __delete_company(self,delete_company_name):

        try:
            sql = f"DELETE FROM companies WHERE company_name = '{delete_company_name}'"

            mycursor.execute(sql)

            mydb.commit()

        except:

            print(f"There is no such company")

    def __get_company_code(self,company_name):

        try:
            mycursor.execute(f"SELECT company_code FROM companies WHERE company_name = '{company_name}'")

            myresult = mycursor.fetchone()

            print(myresult)

        except:

            print(f"Company {company_name} does not exist")


    def __select_family_business(self):
        sql = "SELECT company_name FROM companies WHERE budget <= 10000"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    def get_all_low_class_companies(self):

        try:

          sql = ("SELECT * FROM companies WHERE class_type = 'LOW'")


          mycursor.execute(sql)

          myresult = mycursor.fetchall()

          if myresult == []:
              print("There are no low class companies")
          else:
              for x in myresult:
                  print(x)

        except:

            print("No low class companies registered")

    def get_all_high_class_companies(self):
        try:

           sql = "SELECT * FROM companies WHERE class_type = 'HIGH'"

           mycursor.execute(sql)

           myresult = mycursor.fetchall()

           if myresult == []:
               print("There are no low class companies")
           else:
               for x in myresult:
                   print(x)

        except:

          print("No high class companies registered")

    def get_all_middle_class_companies(self):
        try:

           sql = "SELECT * FROM companies WHERE class_type = 'MIDDLE'"

           mycursor.execute(sql)

           myresult = mycursor.fetchall()

           if myresult == []:
               print("There are no middle class companies")
           else:
               for x in myresult:
                   print(x)

        except:

            print("No middle class companies registered")


    def insert_company(self,i_company_name,budget,class_type):
        return self.__insert_company(i_company_name,budget,class_type)


    def delete_company(self,delete_company_name):
        return self.__delete_company(delete_company_name)

    def get_company_code(self,company_name):
        return self.__get_company_code(company_name)

    def select_family_business(self):
        return self.__select_family_business()

    # def get_all_low_class_companies(self):
    #     return self.__get_all_low_class_companies()

    # def get_all_middle_class_companies(self):
    #     return self.get_all_middle_class_companies()

    # def get_all_high_class_companies(self):
    #     return self.get_all_high_class_companies()



















