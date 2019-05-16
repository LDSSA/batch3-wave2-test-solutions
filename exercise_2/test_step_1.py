import pytest
from all_steps import select_strings


def test_valid_list():
    x = ["hello", "1", 4, "goodbye", None, (1, 2)]
    expected_x = ["hello", "1", "goodbye"]
    error_msg = "Failed with input {}".format(x)
    assert select_strings(x) == expected_x, error_msg


def test_empty_list():
    x = list(range(3))
    expected_x = []
    error_msg = "Failed with input {}".format(x)
    assert select_strings(x) == expected_x, error_msg
