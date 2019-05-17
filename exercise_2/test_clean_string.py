from sorting_words import clean_string


def test_spaces_before_and_uppercase():
    x = "  HELLO"
    expected_x = "hello"

    assert clean_string(x) == expected_x


def test_spaces_and_uppercase():
    x = "   ByE1  "
    expected_x = "bye1"

    assert clean_string(x) == expected_x


def test_two_words():
    x = "ldsa rules"
    expected_x = x

    assert clean_string(x) == expected_x


def test_empty_string():
    x = ""
    expected_x = x

    assert clean_string(x) == expected_x
