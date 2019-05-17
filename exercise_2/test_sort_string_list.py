from sorting_words import sort_string_list


def test_with_chars():
    x = ["a", "d", "c", "b"]
    copy_of_x = x.copy()
    expected_x = ["a", "b", "c", "d"]

    assert sort_string_list(x) == expected_x, error_msg
    assert x == copy_of_x, error_msg


def test_emtpy_list():
    x = []
    copy_of_x = x.copy()
    expected_x = []

    assert sort_string_list(x) == expected_x, error_msg
    assert x == copy_of_x, error_msg


def test_with_words():
    x = ["random", "words", "to", "sort!"]
    copy_of_x = x.copy()
    expected_x = ["random", "sort!", "to", "words"]

    assert sort_string_list(x) == expected_x, error_msg
    assert x == copy_of_x, error_msg
