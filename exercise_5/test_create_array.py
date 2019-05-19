import numpy as np
from numpy_questions import create_array


def test_create_array_valid_shape():
    numbers = [1, 2, 3, 4]
    shape = (2, 2)

    expected_result = np.array([[1, 2], [3, 4]])
    result = create_array(numbers, shape)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)


def test_create_array_invalid_shape():
    numbers = [1, 2, 3, 4]
    shape = (3, 3)

    assert create_array(numbers, shape) is None
