def merge(L1, L2, compareFn):
	'''
	This is the merge section of the merge 
	sort algorithm. This function only merges
	two lists, assuming both are sorted.
	'''
	i, j = 0, 0
	mergedList = []

	while i < len(L1) and j < len(L2):
		if compareFn(L1[i], L2[j]):
			mergedList.append(L1[i])
			i += 1
		else:
			mergedList.append(L2[j])
			j += 1

	# you cannot simply append the lists at the end
	#		since, you need to compare every element
	while i < len(L1):
		mergedList.append(L1[i])
		i += 1
	while j < len(L2):
		mergedList.append(L2[j])
		j += 1

	return mergedList


import operator
def mergeSort(L):
	'''
	This is the function which basically breaks
	down the lists into smaller lists in order
	to sort them.
	'''
	if len(L) < 2:
		return L[:]
	else:
		middle = int(len(L) / 2)
		left = mergeSort(L[:middle])
		right = mergeSort(L[middle:])
		return merge(left, right, operator.lt)





		
# ===============================================================
def merge2(L1, L2, compareFn):
	'''
	The only difference between this and above is
	the appending of remaining elements into the 
	sorted list.
	'''
	i, j = 0, 0
	mergedList = []

	while i < len(L1) and j < len(L2):
		if compareFn(L1[i], L2[j]):
			mergedList.append(L1[i])
			i += 1
		else:
			mergedList.append(L2[j])
			j += 1

	# you cannot simply append the lists at the end
	#		since, you need to compare every element
	#		Here, unlike above, we are using python's 
	#		list comprehensions
	if i < len(L1):
		mergedList.append(L1[i:])
	if j < len(L2):
		mergedList.append(L2[j:])

	return mergedList
