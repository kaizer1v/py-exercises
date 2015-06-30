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
	return fib(n - 1) + fib(n - 2)