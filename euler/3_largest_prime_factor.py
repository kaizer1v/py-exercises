'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of a given number N?
'''


def all_factors(n):
    i = 2
    factors = []
    while i < n // i:
        if n % i == 0:
            if i == n // i:
                factors.append(i)
            else:
                factors.extend([i, n // i])
        i += 1
    return factors


def prime_factors(n):
    i = 2
    factors = []
    while i < n // i:
        if n % i == 0:
            factors.append(i)
        i += 1
    return factors


def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:    # => if n % i != 0
            i += 1   # => i = i + 1
        else:
            n //= i  # => n = n // i
    return n
