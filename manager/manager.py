from myproject.employee.employee import Employee
from myproject.InterfaceEmployee.InterfaceEmployee import LeadPeople,GiveTask,Work

class Manager(Employee,LeadPeople,GiveTask,Work):
    def __init__(self,employee_id,employee_name,employee_type,employee_department,employee_manager_name,department_name):
        super().__init__(employee_id,employee_name,employee_type,employee_department,employee_manager_name)
        self.department_name = department_name

    def give_task(self):
        print("I am the one who is responsible for the task flow!")

    def lead_people(self):
        print("One of my most important skills is to be a good leader")

    def work(self):
        print("I work very hard ten hours a day")
