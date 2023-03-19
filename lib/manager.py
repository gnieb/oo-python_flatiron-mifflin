from lib.employee import Employee

class Manager:

    all = []
    
    def __init__(self, name, department, age ):
        self.name =name
        self.age = age
        self.department = department
        Manager.all.append(self)


    def employees(self):
        employee_list = []
        for employee in Employee.all:
            if employee.manager_name == self:
                employee_list.append(employee)
            return employee_list


    # is this one asking to add an employee instance?? 
    def hire_employees(self, str, num):
        new_employee = Employee(str, num, self )
        return self.employees()
        
    @classmethod
    def all_departments(cls):
        department_list = []
        for manager in Manager.all:
            department_list.append(manager.department)
        return department_list

    @classmethod
    def average_age(cls):
        total = 0
        for element in Manager.all:
            total = element.age + total
        return total/ len(Manager.all)
    
