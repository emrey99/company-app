from myproject.company.company_bl import CompanyBL

list_commands = ["insert powerful company",
                 "insert middle class company",
                 "insert low class company",
                 "insert family business",
                 "show family businesses",
                 "show all low class companies",
                 "show all high class companies",
                 "show all middle class companies",
                 "get employee name",
                 "get info of all employees",
                 "hire employee",
                 "fire employee",
                 "show hr employees",
                 "show developers",
                 "insert task",
                 "delete task",
                 "see employees with task",
                 "see task with employee name",
                 "insert department",
                 "delete department",
                 "get department id"
                 ]
first_command = False
bl = CompanyBL()

while True:
  command = input()
  if command == "help":
    for com in list_commands:
        print(com)
    first_command = True
  else:
      if first_command == False and first_command != "help":
        print("please import 'help' command so you can see all of the commands")
      if command in list_commands:
             if command == "insert powerful company":
                 print("Please write the company name and budget you want to register")
                 inserting_pow_comp = input().split()
                 if type(inserting_pow_comp[0]) == str and type(int(inserting_pow_comp[1])) == int:
                     bl.insert_powerful_company(inserting_pow_comp[0],int(inserting_pow_comp[1]))
                 else:
                     print("please import valid parameters")


             elif command == "insert middle class company":
                 print("Please write the company name and budget you want to register")
                 inserting_pow_comp = input().split()
                 if type(inserting_pow_comp[0]) == str and type(int(inserting_pow_comp[1])) == int:
                     bl.insert_middle_class_company(inserting_pow_comp[0],int(inserting_pow_comp[1]))
                 else:
                     print("please import valid parameters")


             elif command == "insert low class company":
                 print("Please write the company name and budget you want to register")
                 inserting_pow_comp = input().split()
                 if type(inserting_pow_comp[0]) == str and type(int(inserting_pow_comp[1])) == int:
                     bl.insert_low_class_company(inserting_pow_comp[0],int(inserting_pow_comp[1]))
                 else:
                     print("please import valid parameters")


             elif command == "insert family business":
                 print("Please write the company name and budget you want to register")
                 inserting_pow_comp = input().split()
                 if type(inserting_pow_comp[0]) == str and type(int(inserting_pow_comp[1])) == int:
                     bl.insert_family_business(inserting_pow_comp[0],int(inserting_pow_comp[1]))
                 else:
                     print("please import valid parameters")


             elif command == "show family businesses":
                 bl.show_family_businesses()


             elif command == "show developers":
                 bl.show_developers()


             elif command == "show all low class companies":
                 bl.show_all_low_class_companies()


             elif command == "show all middle class companies":
                 bl.show_all_middle_class_companies()


             elif command == "show all high class companies":
                 bl.show_all_high_class_companies()


             elif command == "get employee name":
                 print("Please write the name of employee you want to get")
                 empl = input()
                 if type(empl)==str:
                     bl.get_employee_name(empl)
                 else:
                     print("Please insert a valid name")


             elif command == "get info of all employees":
                  bl.get_info_all_employees()


             elif command == "hire employee":
                 print("Please import information about employee name and employee type , his/hers department name and department id")
                 hire_empl = input().split()
                 try:
                   if type(hire_empl[0]) == str and type(hire_empl[1]) == str and type(hire_empl[2]) == str and type(int(hire_empl[3])) == int:
                     bl.hire_employee(hire_empl[0],hire_empl[1],hire_empl[2],hire_empl[3])
                     print(f"{hire_empl[0]} successfully hired")
                 except:
                     print("Please insert valid parameters to hire employee")


             elif command == "fire employee":#this command does not work properly , needs to be fixed
                 print("Please write the name of the employee you want to fire")
                 fire_empl = input()
                 try:
                     if type(fire_empl) == str:
                         bl.fire_employee(fire_empl)

                 except:
                     print("Please insert a name to fire an employee")


             elif command == "show hr employees":
                 bl.show_hr_employees()


             elif command == "insert task":
                 print("Please insert task name , task desciption , employee name and employee id")
                 inserting_task = input().split()
                 if inserting_task[0].isalpha() and inserting_task[1].isalpha() and inserting_task[2].isalpha() and inserting_task[3].isdigit():
                     bl.inserting_task(inserting_task[0],inserting_task[1],inserting_task[2],inserting_task[3])
                     print("Task inserted successfully")
                 else:
                     print("Please import valid parameters")


             elif command == "delete task":
                 print("Please insert the name of the task you want to delete")
                 del_task = input()
                 if del_task.isalpha():
                     bl.deleting_task(del_task)
                 else:
                     print("Please import valid parameters")


             elif command == "see employees with task":
                 print("Enter a task name")
                 task_n = input()
                 if task_n.isalpha():
                     bl.see_employees_with_task(task_n)
                 else:
                     print("Please enter valid parameters")


             elif command == "see task with employee name":
                 print("Please enter an employee name")
                 empl_n = input()
                 if empl_n.isalpha():
                     bl.see_task_with_employee_name(empl_n)
                 else:
                     print("Please enter valid parameters")


             elif command == "insert department":
                 print("Please insert valid department name , manager name and company code")
                 dep_insert = input().split()
                 if dep_insert[0].isalpha() and dep_insert[1].isalpha() and dep_insert[2].isdigit():
                     bl.insert_department(dep_insert[0],dep_insert[1],dep_insert[2])
                     print("Department successfully inserted")
                 else:
                     print("Please enter valid parameters")


             elif command == "delete department":
                 print("Please enter the name of department you want to delete")
                 del_dep = input()
                 if del_dep.isalpha():
                     bl.delete_department(del_dep)
                 else:
                     print("Please enter valid department name")


             elif command == "get department id":
                 print("Please enter the name of the department you want the id from")
                 dep_get_id = input()
                 if dep_get_id.isalpha():
                     bl.get_department_id(dep_get_id)
                 else:
                     print("Please enter valid department name ")



      else:
          print("There is no such command , please enter a valid command , you can write 'help' to see all commands")
