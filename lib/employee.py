class Employee:
    
    all = []
    
    def __init__(self, name, salary, manager_instance):
        self.name = name
        self.salary = salary
        self.manager_name = manager_instance
        Employee.all.append(self)

    @classmethod
    def paid_over(cls, number):
       paid_over_list = []
       for employee in Employee.all:
            if employee.salary > number:
               paid_over_list.append(employee)
            
            return paid_over_list

    @classmethod
    def find_by_department(cls, dept):
        department_list = []
        for employee in Employee.all:
            if employee.manager_name.department == dept:
                department_list.append(employee)
            return department_list[0]

    def tax_bracket(self):
        bracket_list = []
        for employee in Employee.all:
            if employee.salary > self.salary and employee.salary < self.salary + 1000: 
                bracket_list.append(employee)
            elif employee.salary < self.salary and employee.salary > self.salary - 1000:
                bracket_list.append(employee)
            return bracket_list