import pytest
from orthogonal_arrays import are_orthogonal


def test_are_orthogonal_valid():
    test_cases = [
        {'x': (-1, -2, -3), 'y': (4, 5, 6), 'expected_result': False},
        {'x': (-1, 0), 'y': (0, 1), 'expected_result': True},
        {'x': (-1, 0, 3), 'y': (0, 1), 'expected_result': True},
        {'x': (-1, 0, 3), 'y': (0, 1, 4, 5), 'expected_result': False}
    ]

    for t in test_cases:
        assert are_orthogonal(t['x'], t['y']) == t['expected_result']


def test_are_orthogonal_invalid_1():
    x = (1,)
    y = (2,)

    with pytest.raises(ValueError) as e:
        are_orthogonal(x, y)

    assert str(e.value) == 'Input arrays must have at least two dimensions.'


def test_are_orthogonal_invalid_2():
    x = (1,)
    y = (2, -4, -5)

    with pytest.raises(ValueError) as e:
        are_orthogonal(x, y)

    assert str(e.value) == 'Input arrays must have at least two dimensions.'
