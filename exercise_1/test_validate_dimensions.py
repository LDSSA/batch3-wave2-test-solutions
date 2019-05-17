import pytest
from orthogonal_arrays import validate_dimensions


def test_validate_dimensions_valid():
    x = (-1, -2, -3)
    y = (4, 5, 6)

    assert validate_dimensions(x, y) == [x, y]


def test_validate_dimensions_two_short_tuples():
    x = (1,)
    y = (2,)

    with pytest.raises(ValueError) as e:
        validate_dimensions(x, y)

    assert str(e.value) == 'Input arrays must have at least two dimensions.'


def test_validate_dimensions_one_short_tuple():
    x = (1,)
    y = (2, -4, -5)

    with pytest.raises(ValueError) as e:
        validate_dimensions(x, y)

    assert str(e.value) == 'Input arrays must have at least two dimensions.'


def test_validate_dimensions_long_tuples_1():
    x = (-1, -2, -3, 4)
    y = (4, 5, 6)

    assert validate_dimensions(x, y) == [(-1, -2, -3), y]


def test_validate_dimensions_long_tuples_1():
    x = (-1, -2, -3, 4)
    y = (4, 5, 6, 7, 8, 0)

    assert validate_dimensions(x, y) == [x, (4, 5, 6, 7)]
