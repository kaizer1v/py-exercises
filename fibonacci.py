def fib(n):    # write Fibonacci series up to n
  a, b = 0, 1
  while a < n:
    #print a,
    a, b = b, a+b
#print("Write fibonacci numbers upto")
# n = int(input())
# fib(n)




def recurFib(n):
  """
  assumes n is an integer and >= 0
  returns fibonacci of n
  """
  assert type(n) == int and n >= 0
  if n == 0 or n == 1:
    return 1
  return recurFib(n - 1) + recurFib(n - 2)

'''
The above algorithm is wrong because you are computing
the same fibonacci number twice, when the n-2 becomes the
n-1. Eg: fib(5) is computed twice.

A better way to do this is to use the technique called
memoisation, where you are storing the results and retrieving
if the computation is already done. Let's re-write the
above code to be more efficient
'''

cache = {} # to store already computed values
def cache_fib(num):
  if num not in cache.keys():
    cache[num] = fib_efficient(num)
  return cache[num]

def fib_efficient(n):
  if n < 2:
    return n
  print('>>>>>>', cache)
  return cache_fib(n - 1) + cache_fib(n - 2)

print(fib_efficient(7))



def sumEvenFib():
  """
  By considering the terms in the Fibonacci
  sequence whose values do not exceed four 
  million, find the sum of the even-valued 
  terms.
  """
  a, b, total = 0, 1, 0
  while a < 4000000:
    total += a
    a, b = b, a+b
  return total
