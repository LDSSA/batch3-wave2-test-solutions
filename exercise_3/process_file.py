def process_file(fp, separator):
    total = 0
    for line in fp:
        line_split = line.split(separator)
        line_sum = sum([int(i) for i in line_split[1:]])
        if line_split[0] == '+':
            total += line_sum
        if line_split[0] == '-':
            total -= line_sum

    return total
