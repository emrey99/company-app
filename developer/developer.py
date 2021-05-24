from myproject.employee.employee import EmployeeBL
from myproject.InterfaceEmployee.InterfaceEmployee import DevelopApp,ExecuteTask,Work


class Developer(EmployeeBL,DevelopApp,ExecuteTask,Work):
    def __init__(self,employee_id,employee_name,employee_type,employee_department,employee_manager_name,department_name):
        super().__init__(employee_id,employee_name,employee_type,employee_department,employee_manager_name)
        self.department_name = department_name


    def execute_task(self):
        pass


    def develop_app(self):
        print("My job is to be part of the development team")

    def work(self):
        print("My skill is to stay focused until I get things done")

