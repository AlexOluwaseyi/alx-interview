#!/usr/bin/python3

"""
Given a pile of coins of different values, determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """Function to calculate and find the fewest number
    of coins needed to reach a given amount total
    """
    sorted_coins = sorted(coins, reverse=True)
    lcoins = len(sorted_coins)
    n = 0
    ncoins = 0
    if total <= 0:
        return 0

    while total > 0:
        while n < lcoins:
            if total >= sorted_coins[n]:
                total -= sorted_coins[n]
                ncoins += 1
            else:
                n += 1
        break
    if total == 0:
        return ncoins
    else:
        return -1
