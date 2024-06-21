# #!/usr/bin/python3

# isWinner = __import__('0-prime_game').isWinner


# # print("Winner: {}".format(isWinner(10, [10, 2, 3, 4, 5, 6, 7, 8, 9, 1])))
# # print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
# print("Winner: {}".format(isWinner(10000, [...])))

#!/usr/bin/python3
"""
Main file for testing
"""

isWinner = __import__('0-prime_game').isWinner

nums = [0] * 10000
for i in range(10000):
    nums[i] = i

print("Winner: {}".format(isWinner(10000, nums)))
