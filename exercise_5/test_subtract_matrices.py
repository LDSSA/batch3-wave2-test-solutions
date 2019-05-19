import numpy as np
from numpy_questions import subtract_matrices


def test_subtract_matrices_valid_shapes():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[1, 1], [1, 1]])

    expected_result = np.array([[0, 1], [2, 3]])
    result = subtract_matrices(a, b)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)


def test_subtract_matrices_invalid_shapes():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[1, 1]])

    assert subtract_matrices(a, b) is None
