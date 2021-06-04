from myproject.company.company_db import CompanyDB
from myproject.department.department_db import DepartmentDB
from myproject.employee.employee_db import EmployeeDB
from myproject.task.task_db import TaskDB

class CompanyBL:
    def __init__(self):
        self.comp_db = CompanyDB()
        self.task_db = TaskDB()
        self.dep_db = DepartmentDB()
        self.employee_db = EmployeeDB()

    def insert_powerful_company(self,company_name,company_budget):
        if company_budget >= 1000000:
          self.comp_db.insert_company(company_name,company_budget,class_type="HIGH")
        else:
            print(f"{company_name} cannot be in strong companies list")

    def insert_middle_class_company(self, company_name, company_budget):
        if company_budget >= 100000 and company_budget < 1000000:
            self.comp_db.insert_company(company_name, company_budget,class_type = "MIDDLE")
        else:
            print(f"{company_name} cannot be in middle class companies list")

    def insert_low_class_company(self, company_name, company_budget):
        if company_budget > 10000 and company_budget < 100000:
            self.comp_db.insert_company(company_name, company_budget,class_type = "LOW")
        else:
            print(f"{company_name} cannot be in poor companies list")

    def insert_family_business(self, company_name, company_budget):
        if company_budget <= 10000:
            self.comp_db.insert_company(company_name, company_budget,class_type="FAMILY_BUSINESS")
        else:
            print(f"{company_name} cannot be in family business list")

    def show_family_businesses(self):
        self.comp_db.select_family_business()

    def show_all_low_class_companies(self):
        self.comp_db.get_all_low_class_companies()

    def show_all_high_class_companies(self):
        self.comp_db.get_all_high_class_companies()

    def show_all_middle_class_companies(self):
        self.comp_db.get_all_middle_class_companies()


    def get_employee_name(self,employee_name):
        self.employee_db.get_employee_name(employee_name)


    def get_info_all_employees(self):
        self.employee_db.get_all_employee_names()


    def hire_employee(self,employee_name,employee_type,department_name,department_id):
        self.employee_db.insert_employee(employee_name,employee_type,department_name,department_id)


    def fire_employee(self,employee_name):
        self.employee_db.delete_employee(employee_name)

    def show_hr_employees(self):
        self.employee_db.get_hr_employees()


    def show_developers(self):
        self.employee_db.get_developers()


    def inserting_task(self,task_name, task_description , employee_name ,employee_id):
        self.task_db.insert_task(task_name, task_description , employee_name ,employee_id)

    def deleting_task(self,task_name):
        self.task_db.delete_task(task_name)

    def see_employees_with_task(self,task_name):
        self.task_db.select_employees_with_task(task_name)

    def see_task_with_employee_name(self,employee_name):
        self.task_db.select_task_employees(employee_name)


    def insert_department(self,depart_name,manager_name,company_code):
        self.dep_db.insert_department(depart_name,manager_name,company_code)

    def delete_department(self, depart_name):
        self.dep_db.delete_department(depart_name)

    def get_department_id(self,department_name):
        self.dep_db.get_department_id(department_name)

