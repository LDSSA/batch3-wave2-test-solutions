import math
from perimeter import perimeter


def test_square():
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert perimeter(points) == 4


def test_triangle():
    points = [(0, 0), (3, 0), (1.5, 7)]
    assert math.isclose(perimeter(points), 17.31782, rel_tol=1e-2)


def test_penthagon():
    points = [(-1, -1), (3, -4), (4, 5), (4.5, 7), (-1.5, 10)]
    assert math.isclose(perimeter(points), 33.83649, rel_tol=1e-2)


def test_empty_points():
    points = []
    assert perimeter(points) == 0


def test_single_point():
    points = [(1, 1)]
    assert perimeter(points) == 0


def test_line():
    points = [(1, 1), (2, 2)]
    assert perimeter(points) == 0
