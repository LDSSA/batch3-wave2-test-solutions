class Polygon:
    def __init__(self, points):
        self.points = points

    def area(self):
        raise NotImplementedError("Method area should be defined in the child class.")

    def perimeter(self):
        return compute_perimeter(self.points)
