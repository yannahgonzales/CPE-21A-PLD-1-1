#Application
#Write a Python program that compputes for the area and perimeter of a rectangle
#Use the Shape as parent class
#Use Area() and Perimeter() as methods with its attributes length and width
#Use Rectangle as child class

class Shape:
  def __init__(self,length,width):
    self.length = length
    self.width =  width
  def Area(self):
    return self.length * self.width

  def Perimeter(self):
    return (self.width + self.length) * 2

class Rectangle(Shape):
  pass

rectangle = Shape(10,5)
rectangle2 = Rectangle(10,5)

print("The Area is",(rectangle.Area()))
print("The Perimeter is",(rectangle.Perimeter()))

print("The Area for rectangle2 is",(rectangle2.Area()))
print("The Perimeter for rectangle2 is",(rectangle2.Perimeter()))