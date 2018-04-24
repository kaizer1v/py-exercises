def gcdIter(a, b):
    """
    This is a function to find the
    greatest common divisor for 2 numbers.

    a and b: int >= 0
    ----

    returns: int or float, gcd
    """
    gcd = min(a, b)

    while gcd > 0:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        gcd -= 1


def gcdRecur(a, b):
    """
    This function finds the greatest
    common divisor of two numbers using
    Euclid's theorm / principle. It states
    that:

    About Euclid's gcd algorithm and principle:
    https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example

    if 'b' = 0, then the result is 'a'
    Otherwise, gcd(a, b) is the same as gcd(b, a % b)
    """
    if b == 0:
        return a
    return gcdRecur(b, a % b)
