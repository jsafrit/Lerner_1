def read_n(file_name, num_lines):
    with open(file_name) as f:
        s = []
        x = num_lines
        for line in f:
            s.append(line)
            x -= 1
            if not x:
                yield ''.join(s)
                s = []
                x = num_lines
        yield ''.join(s)


if __name__ == '__main__':
    filename = 'ex2_text.txt'

    for two_lines in read_n(filename, 2):
        print(two_lines)
    print('='*40)
    for four_lines in read_n(filename, 4):
        print(four_lines)
