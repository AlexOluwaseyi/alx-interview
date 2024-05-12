#!/usr/bin/python3

"""
A method that determines if a given data set
represents a valid UTF-8 encoding.

- Prototype: def validUTF8(data)
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need
  to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Function to check if data is a valid utf-8 data
    Checks only the bytes
    """
    i = 0
    while i < len(data):
        byte = data[i]
        num_bytes = 0
        
        # Determine the number of bytes in the current character
        if (byte & 0x80) == 0:
            num_bytes = 1  # 0xxxxxxx
        elif (byte & 0xE0) == 0xC0:
            num_bytes = 2  # 110xxxxx
        elif (byte & 0xF0) == 0xE0:
            num_bytes = 3  # 1110xxxx
        elif (byte & 0xF8) == 0xF0:
            num_bytes = 4  # 11110xxx
        else:
            return False  # Invalid starting byte

        # Check the continuation bytes: they must start with 10xxxxxx
        for j in range(1, num_bytes):
            if i + j >= len(data):
                return False  # Not enough bytes
            if (data[i + j] & 0xC0) != 0x80:
                return False  # Invalid continuation byte

        i += num_bytes  # Move to the next character
    
    return True
