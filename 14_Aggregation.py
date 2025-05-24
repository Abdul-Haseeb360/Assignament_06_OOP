class Employee():
    def __init__(self, name):
        self.name = name


class Department():
    def __init__(self, dept_name):
        self.dept_name = dept_name


employee = Employee("Haseeb")
deparment = Department(employee)
print(deparment.dept_name.name)
