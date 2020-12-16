'''
A palindromic number reads the same both ways.
The smallest 6 digit palindrome made from the product
of two 3-digit numbers is

101101 = 143 * 707

Find the largest palindrome made from the product of
two 3-digit numbers which is less than `N`
'''

n = 100000
i = 100
pairs = []

while i <= (n // i):
    if n % i == 0:
        pairs.append((i, n // i))
    i += 1


m = (0, 0)
for p in pairs:
    if abs(p[0] - p[1]) > abs(m[0] - m[1]):
        m = p
print(m)
