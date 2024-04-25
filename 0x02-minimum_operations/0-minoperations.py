#!/usr/bin/python3

"""
A method that calculates the fewest number
of operations needed to result in exactly
n H characters in the file.
"""


def prime_factors(n):
    """
    Function definition to find
    all prime factors of a number.
    Returns a list of the prime factors.

    Source:
    https://stackoverflow.com/questions/15347174/python-finding-prime-factors
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def count_items(input_list):
    """
    Function definition to create a dictionary using
    the list generated in prime_factors()
    Unique factors are set as keys while the number
    of occurrence are the value.
    """
    result_dict = {}

    for item in input_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1

    return result_dict


def minOperations(n):
    """
    Function definition for minOperations
    Takes a integer value, finds the prime_factors
    and converts prime factors to dict.
    Initializes min_ops to 1 and then performs and
    counts each CopyAll and Paste operations based
    on the value for each each keys in the dict.

    Non-integers and numbers less than or equal to 0
    """
    if type(n) != int or n <= 0:
        return 0
    dct = count_items(prime_factors(n))
    min_ops = 1
    for key, value in dct.items():
        if value == 1:
            min_ops += key
        else:
            min_ops += value + 1

    return min_ops
