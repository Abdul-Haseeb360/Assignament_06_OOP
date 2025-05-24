class Student():
    def __init__(self, name, marks):
        self.name =name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}" , f" Makrs : {self.marks}")

student1 = Student("haseeb", 90)
student1.display()