from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Ractangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return 3.14 * self.width * self.height


reactangle = Ractangle(30, 20)
print(reactangle.area())