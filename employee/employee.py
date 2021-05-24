class Employee:
    def __init__(self,employee_id,employee_name,employee_type,employee_department,employee_manager_name):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_type = employee_type
        self.employee_department = employee_department
        self.employee_manager_name = employee_manager_name



    @property
    def get_department_name(self):
        return self.__employee_department

    @get_department_name.setter
    def get_department_name(self,employee_department_name):
        self.__employee_department = employee_department_name


    @property
    def get_employee_manager_name(self):
        return self.__employee_manager_name

    @get_employee_manager_name.setter
    def get_employee_manager_name(self,employee_manager_name):
        self.__employee_manager_name = employee_manager_name















