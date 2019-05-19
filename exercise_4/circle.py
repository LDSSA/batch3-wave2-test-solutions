import math


# Step 4
class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2
