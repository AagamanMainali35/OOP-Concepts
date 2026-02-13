import math
#Polymorhism 
class Shape:
    
    def draw(self):
        print("Drawing a shape")

# Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        print(f'The area is: {math.pi * self.radius**2:.2f} cm²')

# Rectangle
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        print(f'The area is: {self.length * self.breadth} cm²')

# Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        print(f'The area is: {0.5 * self.base * self.height} cm²')

# Square
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        print(f'The area is: {self.side**2} cm²')
        
class Wheel(Circle):
    def __init__(self,color,brand,radius):
        self.color=color
        self.brand=brand
        super().__init__(radius)
    
Shapes=[Square(3),Rectangle(4,5),Triangle(5,10),Circle(20),Wheel('red','Honda',12)]
for shapes in Shapes:
    shapes.area()
        
