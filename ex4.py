import re


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


def re_line_to_dict(line):
    regexp = '''
        ((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
        .*                              # Junk between IP address and timestamp
        \[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]
        .*                              # Junk between timestamp and request
        "(GET[^"]+)"                    # Request, starting with GET
        '''
    m = re.search(regexp, line, re.X)

    if m:
        ip_address = m.group(1)
        timestamp = m.group(2)
        request = m.group(3)

    else:
        ip_address = 'No IP address found'
        timestamp = 'No timestamp found'
        request = 'No request found'

    output = {'ip_address': ip_address,
              'timestamp': timestamp,
              'request': request}
    return output


def log_to_dict(filename):
    return (re_line_to_dict(line)
            for line in open(filename))


if __name__ == '__main__':
    # result = line_to_dict('mini-access-log.txt')
    result = log_to_dict('mini-access-log.txt')
    for entry in result:
        print(entry)
