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
	This function swaps a given disc like so:
	-> takes the top disc puts it into the spare tower
	-> now takes the 2nd from top disc from that same previous tower and moves it to the target tower
	-> takes that disc from the spare tower and on top of the disc in the target tower
	"""
	if n == 1:
		#base case
		printMove(fr, to)
	else:
		#sub problems
		towers(n - 1, fr, spare, to)
		towers(n - 1, fr, to, spare)
		towers(n - 1, spare, to, fr)