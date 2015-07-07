def cuberoot1():
	x = int(raw_input('Cuberoot of: '))
	for ans in range(0, abs(x) + 1):
		if ans**3 == x:
			break
	if ans**3 != x:
		return '%d is not a perfect cube' % (x)
	elif x < 0:
		ans = -ans
	return 'Cuberoot of %d is %d' % (x, ans)


"""
This method uses the bisectional search algorithm
to find an approximate square root value of a given number.

we are first starting from a middle point between
0 and the given number. We keep find an average that
is always between the low and high and check the square
against that number, until we approximately find one.
"""
def squareroot1():
	x = int(raw_input('Squareroot of: '))
	if x < 0:
		print 'Your number is changed to +%d' % x
		x = abs(x)
	precision = 0.01
	low = 0.0
	high = max(1.0, x)
	ans = (low + high) / 2.0
	while ans**2 - x <= precision:
		if ans**2 > x:
			high = ans
		else:
			low = ans
		ans = (low + high) / 2.0
	return 'Squareroot of %d is approximately %d' % (x, ans)



"""
This method uses the Newton-Raphson method algorithm
to find an approximate square root value of given number.

What is the Newton-Raphson method? It says:

1. Any root can be represented as a polynomial form i.e.
		lets say the square root of 24 can be written as : x^2 - 24 ~= 0 
		A number (x) whose squared is approximately 24.

2. In order to guess a better value (x1) than the previous (x0), Newton-Raphson
		suggests to do the following

							--			 --
							|	 f(x0)	|
		x1 = x0 -	|	 -----	|
							|	 f'(x0)	|
							--			 --

		where f'(x0) is the 1st derivative of the polynomial.

So, for f(x) = x^2 - 24, the first derivative is 2x. lets
say we start guessing the square root of 24 by the number 12.

							--			 --
							|	 f(12)	|
	x1 = 	12 -	|	 -----	|
							|	 f'(12)	|
							--			 --


							--			 		 --
							|	 12^2 - 24	|
		 = 	12 -	|	 ---------	|
							|	 	 2*12		  |
							--			 		 --

		 = 7

Now, repeat this process.

NOTE: the derivative for squareroot will be different from a cuberoot or 
			any other function for that matter. so f(x) and f'(x) will vary
			depending on what you are trying to find.

REFERENCE: http://www.sosmath.com/calculus/diff/der07/der07.html
					 http://web.mit.edu/10.001/Web/Course_Notes/NLAE/node6.html
"""			
def squareroot2(num):
	guess = num / 2.0
	tolerance = 0.01
	while guess**2 - num >= tolerance:
		guess = guess = guess - (((guess**2) - num) / (2*guess))

	return guess


def cuberoot2(num):
	"""
	NOTE: The derivative of x^3 is 3x^2
	"""
	isNeg = False
	epsilon = 0.01

	if num == 0 or num == 1:
		return num
	elif num < 0:
		num = abs(num)
		isNeg = True

	guess = num / 2.0

	while abs(guess**3 - num) >= epsilon:
		guess = guess - (((guess**3) - num) / (3 * (guess**2)))
		print guess

	if isNeg == True:
		return (-1 * guess)
	else:
		return guess