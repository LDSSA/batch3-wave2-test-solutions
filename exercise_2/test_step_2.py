from all_steps import clean_string


def test_spaces_before_and_uppercase():
    x = "  HELLO"
    expected_x = "hello"
    error_msg = "Failed with input {}".format(x)
    assert clean_string(x) == expected_x, error_msg


def test_spaces_and_uppercase():
    x = "   ByE1  "
    expected_x = "bye1"
    error_msg = "Failed with input {}".format(x)
    assert clean_string(x) == expected_x, error_msg


def test_two_words():
    x = "ldsa rules"
    expected_x = x
    error_msg = "Failed with input {}".format(x)
    assert clean_string(x) == expected_x, error_msg


def test_empty_string():
    x = ""
    expected_x = x
    error_msg = "Failed with input {}".format(x)
    assert clean_string(x) == expected_x, error_msg
