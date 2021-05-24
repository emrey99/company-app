from myproject.employee.employee import Employee
from myproject.InterfaceEmployee.InterfaceEmployee import SignDoc,RecruitPeople,Work


class HR(Employee,SignDoc,RecruitPeople,Work):
    def __init__(self,employee_id,employee_name,employee_type,employee_department,employee_manager_name,department_name):
        super().__init__(employee_id,employee_name,employee_type,employee_department,employee_manager_name)
        self.department_name = department_name

    def sign_doc(self):
        print("My main task is to sign docs")

    def recruit_people(self):
        pass

    def work(self):
        print("My working hours are very flexibly and I do not have an exact schedule")
