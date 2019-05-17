import io
from process_file import process_file


in_out_ok = {
    (("+", 3, 4, 10), ("+", 1)): 18,
    (("+", 3, 4, 5), ("-", 2, 6)): 4,
    (("+", 1, 1), ("-", 5)): -3,
    (("-", 1, 1, 3),): -5,
    (("-", 11, 4), ('+', 15)): 0,
    (("-", 11, 4), ('+', 15), ('=', 10)): 0,
}


def mock_fp(input_, separator):
    lines = '\n'.join([separator.join(str(char) for char in raw_line) for raw_line in input_])
    return io.StringIO(lines)


def process_file_(fp, separator):
    result = 0
    lines = [line.split(separator) for line in fp.readlines()]
    print(lines)
    for line in lines:
        line_sum = sum(int(c) for c in line[1:])
        if line[0] == '+':
            result += line_sum
        if line[0] == '-':
            result -= line_sum
        # anything else is ignored
    return result


def err_msg(input_, separator, outpout_, computed):
    return f"""

        data used to generate file: {input_}

        with separator: "{separator}"

        ERROR!

        expected: {outpout_}

        got: {computed}

        """


def test_process_file(in_out):
    for i, o in in_out.items():
        for separator in [' ', ',', '::']:
            fp = mock_fp(i, separator)
            computed = process_file(fp, separator)
            assert computed == o, err_msg(i, separator, o, computed)


test_process_file(in_out_ok)
