#!/usr/bin/python3

"""A prime game
"""


'''
# Without Sieve of Eratosthenes
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


# With Sieve of Eratosthenes
def sieve(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def simulate_game(n):
    primes = sieve(n)
    if not primes:
        return 'Ben'

    moves = 0
    remaining = set(range(1, n + 1))

    for prime in primes:
        if prime in remaining:
            multiples = set(range(prime, n + 1, prime))
            remaining -= multiples
            moves += 1

    return 'Maria' if moves % 2 != 0 else 'Ben'


def isWinner(x, nums):
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

'''
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
         # Log the current state of the list
         print(f"Current list: {remaining}")

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
         # Logging the current move
         print(f"{current_turn} picks {prime}")
         # Remove the prime and its multiples
         removed = [num for num in remaining if num % prime == 0]
         remaining = [num for num in remaining if num % prime != 0]
         # Logging the removed numbers
         print(f"Removed numbers: {removed}")
         # Switch turn
         current_turn = 'Ben' if current_turn == 'Maria' else 'Maria'
 def isWinner(x, nums):
     """Determine the player that won the most rounds."""
     maria_wins = 0
     ben_wins = 0
     for n in nums:
         print(f"Starting game with n = {n}")
         winner = simulate_game(n)
         print(f"Winner of this round: {winner}\n")
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
 # Test match where Maria wins
 if __name__ == "__main__":
     print("Overall Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
'''
