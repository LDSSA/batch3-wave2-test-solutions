import pytest
from polygon import Polygon


def test_polygon_class():
    points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    polygon = Polygon(points)

    assert isinstance(polygon, Polygon)
    assert isinstance(polygon.points, list)
    assert polygon.points == points


def test_area():
    points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    polygon = Polygon(points)

    with pytest.raises(NotImplementedError) as e:
        polygon.area()

    assert str(e.value) == 'Method area should be defined in the child class.'


def test_perimeter():
    points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    polygon = Polygon(points)

    assert polygon.perimeter() == 8


def test_polygon_empty_points():
    points = []
    polygon = Polygon(points)

    assert isinstance(polygon, Polygon)
    assert isinstance(polygon.points, list)
    assert polygon.points == points
    assert polygon.perimeter() == 0


def test_polygon_2_points():
    points = [(0, 0), (10, 9)]
    polygon = Polygon(points)

    assert isinstance(polygon, Polygon)
    assert isinstance(polygon.points, list)
    assert polygon.points == points
    assert polygon.perimeter() == 0
