from sorting_words import sort_this


def test_list_with_none():
    x = [" Aleluia", 1, "None!   ", None]
    expected_x = ["aleluia", "none!"]

    assert sort_this(x) == expected_x


def test_empty_list():
    x = []
    expected_x = []

    assert sort_this(x) == expected_x


def test_list_with_tuple():
    x = [1, "words", "    to", (1, 2)]
    expected_x = ["to", "words"]

    assert sort_this(x) == expected_x


def test_list_without_strings():
    x = [1, 2, 3]
    expected_x = []

    assert sort_this(x) == expected_x
