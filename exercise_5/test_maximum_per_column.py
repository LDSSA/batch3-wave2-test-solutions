import numpy as np
from numpy_questions import maximum_per_column


def test_maximum_per_column_2_rows():
    a = np.array([[1, 2], [3, -5]])
    expected_result = np.array([3, 2])
    result = maximum_per_column(a)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)


def test_maximum_per_column_3_rows():
    a = np.array([[1, -2], [0, 4], [6, -10]])
    expected_result = np.array([6, 4])
    result = maximum_per_column(a)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)
