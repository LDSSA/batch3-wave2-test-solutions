from orthogonal_arrays import inner_product


def test_inner_product_valid():
    x = (-1, -2, -3)
    y = (4, 5, 6)

    assert inner_product(x, y) == -32


def test_inner_product_valid_zero():
    x = (-1, -2, -2)
    y = (4, 0, -2)

    assert inner_product(x, y) == 0
