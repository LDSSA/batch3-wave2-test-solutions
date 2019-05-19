import numpy as np
from polygon import Polygon


# this function was given in the exercise
def euclidean_distance(a, b):
    array_a = np.array(a)
    array_b = np.array(b)

    return np.linalg.norm(array_a - array_b)


# Step 3
class Square(Polygon):
    def area(self):
        side = euclidean_distance(self.points[0], self.points[1])

        return side**2
