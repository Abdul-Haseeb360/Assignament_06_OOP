class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary


emp1 = Employee("John", 30, 50000)
print(emp1.name)
print(emp1._age)
print(emp1.__salary)



# I created an Employee class with public, protected, and private variables. 
# I was able to access the public variable directly. 
# The protected variable was also accessible but is marked for internal use. 
# However, trying to access the private variable directly gave an AttributeError.
# I could still access it using name mangling(_ClassName__var), but it is not recommended as it breaks encapsulation.
