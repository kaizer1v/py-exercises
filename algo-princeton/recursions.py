'''
factorial of a number
'''
def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n - 1)




'''
Euclid's algorithm to get GCD between two numbers
if for two numbers p & q and if p > q, then the GCD of p & q
is the same as GCD of q & p % q
'''
def gcd(p, q):
  if q == 0:
    return p
  return gcd(q, p % q)





'''
convert any number into binary
'''
def convertToBinary(n):
  if n == 0:                      # base case
    return
  convertToBinary(n // 2)         # reduction step 
  print(n % 2)





'''
Compose a program that takes a command-line argument n and writes all n!
permutations of the n letters starting at a (assume that n is
no greater than 26)
'''
fib_cache = {}
def fib(n):
  # if the value is cached, return it
  if n in fib_cache:
    return fib_cache[n]

  # compute the value & then return it
  if n <= 2:
    value = n
  else:
    value = fib(n - 1) + fib(n - 2)

  fib_cache[n] = value
  return value





'''
check if two numbers are relatively prime
i.e. two numbers are relatively prime when the only common
factor between them is 1
'''
def is_relatively_prime(p, q):
  if q == 0:
    return p == 1
  return is_relatively_prime(q, p % q)





'''
compute sum of n numbers

sum(10) = 10 * sum(9)
'''
def prod_of_nums(n):
  if n == 1:
    return 1
  return n * prod_of_nums(n - 1)





'''
T(n) = T(n/2) + 1
T(n) = 2T(n/2) + 1
T(n) = 2T(n/2) + n
T(n) = 4T(n/2) + 3
'''
def T(n):
  if n <= 1:
    return 1
  v1 = T(n/2) + 1
  v2 = 2 * T(n/2) + 1
  v3 = 2 * T(n/2) + n
  v4 = 4 * T(n/2) + 3
  print(v1, v2, v3, v4)
  return





'''
argument n and writes all n! permutations of the n letters starting at a
(assume that n is no greater than 26)

n = 2 i.e. ab         2! = 2
returns = `ab ba`
'''
def permutations(s):
  if len(s) == 1:
    return s

  to_return = []
  for i in range(len(s)):
    substrs = permutations(s[:i] + s[i + 1:])

    for substr in substrs:
      to_return.append(s[i] + substr)

  return to_return





'''
writes the increase in processor speed over a decade if processor speed
doubles every n months
'''
def mooreslaw(every=15, months=120):
  speed = 1
  for i in range(months // every):
    speed = 2 * speed
  return speed




'''
Design a linear algorithm that finds a contiguous subsequence of at most m in a
sequence of n integers that has the highest sum among all such subsequences.
Implement your algorithm, and confirm that the order of growth of its running
time is linear.
'''
def msum(l, m):
  n = len(l)
  maxsum = 0
  seq = []
  if m > n:
    return l
  for i in range(n):
    if sum(l[i:i + m]) > maxsum:
      maxsum = sum(l[i:i + m])
      seq = [l[i:i + m]]
    elif sum(l[i:i + m]) == maxsum:
      seq.append(l[i:i + m])
  return seq





def recursive(i):
  if i <= 0:
    return i
  else:
    o = recursive(i - 1)
  return o




def main():
    # print(factorial(5))
    # print(gcd(1440, 408))
    # print(convertToBinary(1242))      # 10011011010
    # print(i, ': ', fib(i))
    # print(prod_of_nums(1))
    # print(T(24))
    # print(permutations('abc'))
    # print(msum([4, 1, 9, 6, 3, 5, 9], 3))
    print(recursive(3))

if __name__ == '__main__':
    main()
