class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        return f"{self.name} is barking"

dog = Dog("Tomy", "German Shepherd")
print(dog.bark())