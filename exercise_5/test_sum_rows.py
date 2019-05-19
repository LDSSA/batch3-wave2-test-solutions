import numpy as np
from numpy_questions import sum_rows


def test_sum_rows_2_rows():
    a = np.array([[1, 2], [3, 4]])
    expected_result = np.array([3, 7])
    result = sum_rows(a)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)


def test_sum_rows_3_rows():
    a = np.array([[1, -2], [0, 4], [6, -10]])
    expected_result = np.array([-1, 4, -4])
    result = sum_rows(a)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)
