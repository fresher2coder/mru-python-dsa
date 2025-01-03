from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Abstract class usage
rectangle = Rectangle(10, 5)
print(f"Area of rectangle: {rectangle.area()}")  # Output: Area of rectangle: 50
