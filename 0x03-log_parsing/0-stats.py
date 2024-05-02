#!/usr/bin/python3

"""
"""

import re
import fileinput
import signal
import sys


status_record = dict(sorted({}))
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
    # status_code = re.search(status_code_pattern, line).group()
    # size = int(re.search(size_pattern, line).group())
    global file_size

    status_code = line.split()[-2]
    size = int(line.split()[-1])

    if status_code not in status_record.keys():
        status_record[status_code] = 1
    else:
        status_record[status_code] += 1
    file_size += size

    return file_size


def printer(status_record):
    total_freq = 0
    global file_size
    # sorted_dict = dict(sorted(status_record.items()))

    for value in status_record.values():
        total_freq += value
    if total_freq % 10 == 0:
        print(f'File size: {file_size}')
        for key, value in status_record.items():
            print(f'{key}: {value}')

def signal_handler(signal, frame):
    print(f'File size: {file_size}')
    for key, value in status_record.items():
        print(f'{key}: {value}')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in fileinput.input():
    line = line.strip('\n\r')
    get_essentials(line)
    printer(status_record)
