# In order to make this class Shape as an abstract class, you need
# to make this class as an instance of another class called ABCMeta
# which is available in Python

# Above statement is further explained here: This is done so that 
# for every shape there is a method called area() which computes the
# area of that shape

# Abstract base class does not have definitions on its own, it will 
# only contain abstract methods

from abc import ABCMeta, abstractmethod

# Now class Shape is an instance of ABCMeta class
class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of square: ", self.side * self.side)
        
class Rectangle(Shape):
    width = 5
    length = 10
    def area(self):
        print("Area of rectangle: ", self.width * self.length)
         
square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
