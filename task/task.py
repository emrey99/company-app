class Task:
    def __init__(self,task_name,task_description,task_id,task_employee_name):
        self.task_name = task_name
        self.task_description = task_description
        self.task_id = task_id
        self.task_employee_name = task_employee_name


    @property
    def get_task_name(self):
        return self.__task_name

    @get_task_name.setter
    def get_task_name(self,task_name):
        self.__task_name = task_name

    @property
    def get_task_description(self):
        return self.__task_description

    @get_task_description.setter
    def get_task_description(self,task_description):
        self.__task_description = task_description

    @property
    def get_task_employee_name(self):
        return self.__task_employee_name

    @get_task_employee_name.setter
    def get_task_employee_name(self,task_employee_name):
        self.__task_employee_name = task_employee_name






