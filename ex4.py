def line_to_dict(filename):
    result_list = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line_fields = line.split(' ', maxsplit=5)

            # IP address is easy, first field
            line_dict = {'ip_address': line_fields[0]}

            # combine 2 timestamp fields and strip off the outside brackets
            line_dict['timestamp'] = line_fields[3][1:] + ' ' + line_fields[4][:-1]

            # strip starting quote, find closing quote, and only use in between
            request = line_fields[5][1:]
            line_dict['request'] = request[:request.find('"')]

            result_list.append(line_dict)
    return result_list


if __name__ == '__main__':
    result = line_to_dict('mini-access-log.txt')
    for entry in result:
        print(entry)
