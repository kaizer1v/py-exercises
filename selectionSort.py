'''
This algorithm has a bigOh of O(L^2) complexity.
'''

def selectionSort(L):
	'''
	Assume L is a list of elements that can be compared
	with '>' operator, this function will sort L in ascending
	order
	'''
	prefix = 0
	while prefix != len(L):
		for i in range(prefix, len(L)):
			if L[i] < L[prefix]:
				L[prefix], L[i] = L[i], L[prefix]
		prefix += 1

	return L