import pytest
from orthogonal_arrays import validate_tuples


def test_validate_tuples_valid():
    x = (1, 2, 3)
    y = (4, 5, 6)

    assert validate_tuples(x, y)


def test_validate_tuples_invalid():
    x = 1
    y = 'hello'

    with pytest.raises(ValueError) as e:
        validate_tuples(x, y)

    assert str(e.value) == 'The input arguments must be tuples.'
