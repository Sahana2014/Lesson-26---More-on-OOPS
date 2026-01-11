import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Get input from user
r = float(input("Enter the radius of the circle: "))
circle = Circle(r)

# Using + to concatenate strings
print("Area of the circle: " + str(circle.area()))
print("Perimeter of the circle: " + str(circle.perimeter()))