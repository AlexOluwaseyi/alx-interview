#!/usr/bin/python3

"""
script that reads stdin line by line and computes metrics:

- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size>
  (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C),
  print these statistics from the beginning:
- Total file size: File size: <total size>
- where <total size> is the sum of all previous <file size>
  (see input format above)
- Number of lines by status code:
  - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
  - if a status code doesn’t appear or is not an integer,
    don’t print anything for this status code
  - format: <status code>: <number>
  - status codes should be printed in ascending order
"""

import re
import fileinput
import signal
import sys


status_record = {}
sorted_dict = {}
file_size = 0

# Regex patterns
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
date_pattern = r'\[(.*?)\]'
method_url_pattern = r'"(.*?)"'
status_code_pattern = r'(\d{3})'
size_pattern = r'(\d+)$'


def get_essentials(line):
    """
    Extract status_code and file_size from each line
    Performed after line.split() operation
    """
    global file_size

    status_code = line.split()[-2]
    size = int(line.split()[-1])

    if not status_code.isdigit():
        return None

    status_code = int(status_code)

    if status_code not in status_record.keys():
        status_record[status_code] = 1
    else:
        status_record[status_code] += 1
    file_size += size

    return file_size


def printer(status_record):
    """
    function to print cummulative file_size and
    sorted dict of status code frequency
    """
    total_freq = 0
    global file_size

    for value in sorted_dict.values():
        total_freq += value
    if total_freq % 10 == 0:
        print(f'File size: {file_size}')
        for key, value in sorted_dict.items():
            print(f'{key}: {value}')


def signal_handler(signal, frame):
    """
    Function to handle KeyboardInterrupt (^C)
    """
    print(f'File size: {file_size}')
    for key, value in sorted_dict.items():
        print(f'{key}: {value}')
    sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)


def execution():
    """
    Function to read line from stdin and call other functions
    """
    signal.signal(signal.SIGINT, signal_handler)

    global status_record
    global sorted_dict
    for line in fileinput.input():
        line = line.strip('\n\r')
        get_essentials(line)
        sorted_dict = dict(sorted(status_record.items()))
        printer(sorted_dict)


if __name__ == "__main__":
    """Call to execution() function here"""
    execution()
