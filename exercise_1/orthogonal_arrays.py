# Step 1
def validate_tuples(a, b):
    if (not isinstance(a, tuple)) or (not isinstance(b, tuple)):
        raise ValueError("The input arguments must be tuples.")

    return True


# Step 2
def validate_dimensions(a, b):
    if (len(a) < 2) or (len(b) < 2):
        raise ValueError("Input arrays must have at least two dimensions.")

    min_dims = min(len(a), len(b))

    return [a[:min_dims], b[:min_dims]]


# Step 3
def inner_product(a, b):
    return sum([x_i * y_i for x_i, y_i in zip(a, b)])


# Step 4
def are_orthogonal(x, y):
    validate_tuples(x, y)
    x, y = validate_dimensions(x, y)

    return inner_product(x, y) == 0
