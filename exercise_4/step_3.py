class Square(Polygon):
    def area(self):
        side = euclidean_distance(points[0], points[1])

        return side**2
