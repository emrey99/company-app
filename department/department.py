class Department:
    def __init__(self,employee,dep_name,dep_id):

        self.employee = employee
        self.dep_name = dep_name
        self.dep_id = dep_id


    @property
    def get_employee_name(self):
        return self.__employee

    @get_employee_name.setter
    def get_employee_name(self,employee_name):
        self.__employee = employee_name

    @property
    def get_department_name(self):
        return self.__dep_name

    @get_department_name.setter
    def get_department_name(self,department_name):
        self.__dep_name = department_name

    @property
    def get_department_id(self):
        return self.__dep_id

    @get_department_id.setter
    def get_department_id(self,department_id):
        self.__dep_id = department_id










