def isPalindrome(str):
	"""
	This function checks for any given string
	whether it is a palindrome or not. If it is
	this returns true, false otherwise.

	we have used recurssion to solve this problem.

	TestCases:
		a
		a-a
		nitin
		abccba
		xyzyy
		keviv
	"""

	def isChar(str):
		str = str.lower()
		ans = ''
		for s in str:
			if s in 'abcdefghijklmnopqrstuvwxyz':
				ans = ans + s
		return ans

	def isPal(str):
		if len(str) <= 1:
			return True
		else:
			return str[0] == str[-1] and isPal(str[1:-1])

	return isPal(isChar(str))