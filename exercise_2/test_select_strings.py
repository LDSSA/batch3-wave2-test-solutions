import pytest
from sorting_words import select_strings


def test_valid_list():
    x = ["hello", "1", 4, "goodbye", None, (1, 2)]
    expected_x = ["hello", "1", "goodbye"]

    assert select_strings(x) == expected_x


def test_empty_list():
    x = list(range(3))
    expected_x = []

    assert select_strings(x) == expected_x
