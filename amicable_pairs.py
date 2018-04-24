def factors2(x):
    '''
    This function takes a
    number and #prints the factors
    '''
    factors = []
    total = 0
    for i in range(1, x):
        if x % i == 0:
            total += i
            factors.append(i)
    return (factors, total)


def sum_of_factors(n):
    '''
    Given a number n, find the
    sum of all the proper factors
    '''
    return factors2(n)[1]


def amicable_numbers(n):
    if n == sum_of_factors(sum_of_factors(n)):
        return (n, sum_of_factors(n))  # amicable numbers


def gen_amicable_pairs(upto):
    '''
    Let d(n) be defined as the sum
    of proper divisors of n
    (numbers less than n which
      divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b,
    then a and b are an amicable pair and
    each of a and b are called amicable numbers.

    For example, the proper divisors
    of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of
    284 are 1, 2, 4, 71 and 142; so d(284) = 220.
    '''
    to_return = []
    for i in range(1, upto):
        if amicable_numbers(i) is not None:
            to_return.append(amicable_numbers(i))
    return to_return


print(gen_amicable_pairs(220))
print(gen_amicable_pairs(1513))
