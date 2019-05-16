from all_steps import sort_string_list


def test_with_chars():
    x = ["a", "d", "c", "b"]
    copy_of_x = x.copy()
    expected_x = ["a", "b", "c", "d"]

    error_msg = "Failed with input {}".format(x)
    assert sort_string_list(x) == expected_x, error_msg
    error_msg = "Failed with input {}. The original array was changed!".format(x)
    assert x == copy_of_x, error_msg


def test_emtpy_list():
    x = []
    copy_of_x = x.copy()
    expected_x = []
    error_msg = "Failed with input {}".format(x)
    assert sort_string_list(x) == expected_x, error_msg
    error_msg = "Failed with input {}. The original array was changed!".format(x)
    assert x == copy_of_x, error_msg


def test_with_words():
    x = ["random", "words", "to", "sort!"]
    copy_of_x = x.copy()
    expected_x = ["random", "sort!", "to", "words"]
    error_msg = "Failed with input {}".format(x)
    assert sort_string_list(x) == expected_x, error_msg
    error_msg = "Failed with input {}. The original array was changed!".format(x)
    assert x == copy_of_x, error_msg
