import math
from circle import Circle


def test_circle_class():
    centre = (1, 1)
    radius = 3
    circle = Circle(centre, radius)

    assert isinstance(circle, Circle)
    assert isinstance(circle.centre, tuple)
    assert circle.centre == centre
    assert circle.radius == radius


def test_area():
    centre = (1, 1)
    radius = 3
    circle = Circle(centre, radius)

    assert math.isclose(circle.area(), 28.27433, rel_tol=1e-2)


def test_perimeter():
    centre = (1, 1)
    radius = 3
    circle = Circle(centre, radius)

    assert math.isclose(circle.perimeter(), 18.84955, rel_tol=1e-2)


def test_circle_zero_radius():
    centre = (1, 1)
    radius = 0
    circle = Circle(centre, radius)

    assert circle.perimeter() == 0
    assert circle.area() == 0
