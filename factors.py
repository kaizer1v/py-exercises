def #print_factors(x):
    '''
    This function takes a
    number and #prints the factors
    '''
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)


def factors(n):
    return [(i, n // i) for i in range(1, int(n**0.5) + 1) if n % i == 0]
    #[y if i else x/y for y in range(1, sqrt(x)+1) for i in 0,1 if x%y == 0]


# Usage
#print factors(135125)
#print factors(1331)
