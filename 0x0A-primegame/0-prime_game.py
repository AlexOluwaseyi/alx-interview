#!/usr/bin/python3

"""A prime game
"""


def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def simulate_game(n):
    """Simulate a single game for given n and return the winner."""
    remaining = list(range(1, n + 1))
    current_turn = 'Maria'

    while True:
        # Find the first prime in the remaining numbers
        prime_found = False
        for num in remaining:
            if is_prime(num):
                prime = num
                prime_found = True
                break

        if not prime_found:
            # No prime found means current player loses
            return 'Ben' if current_turn == 'Maria' else 'Maria'

        # Remove the prime and its multiples
        remaining = [num for num in remaining if num % prime != 0]

        # Switch turn
        current_turn = 'Ben' if current_turn == 'Maria' else 'Maria'


def isWinner(x, nums):
    """Determine the player that won the most rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None


'''
def isWinner(x, nums):
    maria_score = 0
    ben_score = 0

    for num in nums:
        primes = [True for i in range(max(nums) + 1)]
        primes[0] = primes[1] = False
        prime_count = 0

        for i in range(2, int(len(primes) ** 0.5) + 1):
            if primes[i]:
                prime_count += 1
                for j in range(i*i, len(primes), i):
                    primes[j] = False

        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    else:
        return None


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
    winner = None
    nums_list = nums[:]
    # check if there is a prime number in nums_list
    for i in nums_list:
        if is_prime(i):
            # next turn
            break
        else:
            # declare winner
            pass
    for rounds in range(x):
        pass


def gameplay():
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
'''
