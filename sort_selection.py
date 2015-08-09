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





def selectionSort2(L):

	# assume a sorted part of the list's index
	lastSortedIndex = 0

	# from the last sorted index, until the end of the list
	while lastSortedIndex < len(L):

		# loop through every element
		for currIndex in range(lastSortedIndex + 1, len(L)):

			# and if you find any element which is less than the last sorted element.
			if L[currIndex] < L[lastSortedIndex]:
				# then swap it
				L[currIndex], L[lastSortedIndex] = L[lastSortedIndex], L[currIndex]

		# Now, increment the last sorted index by 1
		lastSortedIndex += 1

	# Finally, return the sorted list
	return L