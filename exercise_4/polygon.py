from perimeter import perimeter as compute_perimeter


# Step 2
class Polygon:
    def __init__(self, points):
        self.points = points

    def area(self):
        msg = 'Method area should be defined in the child class.'
        raise NotImplementedError(msg)

    def perimeter(self):
        return compute_perimeter(self.points)
