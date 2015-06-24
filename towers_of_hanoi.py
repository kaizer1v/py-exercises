"""
About Towers of Hanoi
"""

def printMove(fr, to):
	"""
	Simply prints the steps that you are executing
	"""
	print 'Move from ', str(fr), ' to ', str(to)


def towers(n, fr, to, spare):
	"""
	
	"""
	if n == 1:
		#base case
		printMove(fr, to)
	else:
		#sub problems
		towers(n - 1, fr, spare, to)
		towers(n - 1, fr, to, spare)
		towers(n - 1, spare, to, fr)