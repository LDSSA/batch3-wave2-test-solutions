import io
from process_file import process_file


def mock_fp(test_input, separator):
    lines_list = [
        separator.join(str(item) for item in raw_line)
        for raw_line in test_input
    ]
    lines = '\n'.join(lines_list)

    return io.StringIO(lines)


def get_error_msg(test_input, separator, expected_output, computed):
    return (
        f"data used to generate file: {test_input}\n"
        f'with separator: "{separator}"\n'
        'ERROR!'
        f"expected: {expected_output}\n"
        f"got: {computed}"
    )


def test_process_file():
    test_cases = {
        (("+", 3, 4, 10), ("+", 1)): 18,
        (("+", 3, 4, 5), ("-", 2, 6)): 4,
        (("+", 1, 1), ("-", 5)): -3,
        (("-", 1, 1, 3),): -5,
        (("-", 11, 4), ('+', 15)): 0,
        (("-", 11, 4), ('+', 15), ('=', 10)): 0,
    }
    separators = [' ', ',', '::']

    for test_input, expected_output in test_cases.items():
        for sep in separators:
            fp = mock_fp(test_input, sep)
            answer = process_file(fp, sep)

            error_msg = get_error_msg(test_input, sep, expected_output, answer)
            assert answer == expected_output, error_msg
