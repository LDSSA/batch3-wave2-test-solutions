from square import Square, Polygon


def test_square_class():
    points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    square = Square(points)

    assert isinstance(square, Square)
    assert issubclass(Square, Polygon)
    assert isinstance(square.points, list)
    assert square.points == points


def test_area():
    points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    square = Square(points)

    assert square.area() == 4


def test_perimeter():
    points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    square = Square(points)

    assert square.perimeter() == 8
