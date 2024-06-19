#!/usr/bin/python3

"""A prime game
"""

def isWinner(x, nums):
    """
    Prototype: def isWinner(x, nums)
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """
    turn = 'Maria'
    for rounds in range(x):

        pass


def next_turn(current_turn):
    """Changes turn to the next player
    """
    if current_turn == 'Maria':
        return 'Ben'
    return 'Maria'


def is_prime(num):
    """Checks if a number is prime
    """
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                break
        else:
            return True
    return False


if __name__ == "__main__":
    turn = 'Ben'
    turn = next_turn(turn)
    print(turn)
    turn = next_turn(turn)
    print(turn)