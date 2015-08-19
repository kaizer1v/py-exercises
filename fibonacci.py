def fib(n):    # write Fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b
print("Write fibonacci numbers upto")
n = int(input())
fib(n)




def recurFib(n):
	"""
	assumes n is an integer and >= 0
	returns fibonacci of n
	"""
	assert type(n) == int and n >= 0
	if n == 0 or n == 1:
		return 1
	return recurFib(n - 1) + recurFib(n - 2)




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