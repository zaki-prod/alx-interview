#!/usr/bin/python3
'''Prime Game'''

def isWinner(x, nums):
    '''Determines the overall winner of the game.'''
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to precompute primes
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute prime counts up to each number
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:  # Odd count -> Maria wins
            maria_wins += 1
        else:  # Even count -> Ben wins
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve_of_eratosthenes(max_n):
    '''Generates a list of primes up to max_n using the Sieve of Eratosthenes.'''
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    return primes

