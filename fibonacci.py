def fib(n):    # write Fibonacci series up to n
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a+b
print("Write fibonacci numbers upto")
n = int(input())
fib(n)
