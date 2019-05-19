import numpy as np


# Step 1
def create_array(numbers, shape):
    if len(numbers) != shape[0] * shape[1]:
        return None

    return np.array(numbers).reshape(shape)


# This solution was also valid for Step 1
def create_array_aternative(numbers, shape):
    n_elements = shape[0] * shape[1]
    if len(numbers) < n_elements:
        return None

    if len(numbers) > n_elements:
        numbers = numbers[:n_elements]

    return np.array(numbers).reshape(shape)


# Step 2
def subtract_matrices(a, b):
    if a.shape != b.shape:
        return None

    return a - b


# Step 3
def sum_rows(a):
    return a.sum(axis=1)


# Step 4
def maximum_per_column(x):
    return x.max(axis=0)


# Step 5
def replace_negatives(x, replacement):
    return np.where(x > 0, x, replacement)
