import numpy as np
from numpy_questions import replace_negatives


def test_replace_negatives_1():
    a = np.array([[1, 2], [3, -5]])
    b = 100
    original_a = a.copy()

    expected_result = np.array([[1, 2], [3, 100]])
    result = replace_negatives(a, b)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)

    error_msg = 'The original array has changed'
    assert np.array_equal(a, original_a), error_msg


def test_replace_negatives_2():
    a = np.array([[-100, 2], [3.1, -5]])
    b = 7
    original_a = a.copy()

    expected_result = np.array([[7, 2], [3.1, 7]])
    result = replace_negatives(a, b)

    assert isinstance(result, np.ndarray)
    assert np.array_equal(result, expected_result)

    error_msg = 'The original array has changed'
    assert np.array_equal(a, original_a), error_msg
