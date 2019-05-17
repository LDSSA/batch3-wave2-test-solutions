def select_strings(l):
    return [i for i in l if isinstance(i, str)]


def clean_string(x):
    return x.strip().lower()


def sort_string_list(l):
    return sorted(l)


def sort_this(l):
    return sort_string_list([clean_string(i) for i in select_strings(l)])
