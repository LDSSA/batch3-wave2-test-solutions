# Step 1
def select_strings(l):
    return [i for i in l if isinstance(i, str)]


# Step 2
def clean_string(x):
    return x.strip().lower()


# Step 3
def sort_string_list(l):
    return sorted(l)


# Step 4
def sort_this(l):
    return sort_string_list([clean_string(i) for i in select_strings(l)])
