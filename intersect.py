def intersect(L1, L2):
	'''
	Assumes L1 and L2 are lists.
	Returns a unique list of all the elements that 
	in L1 and L2 both.
	'''
	if len(L1) == 0 and len(L2) == 0:
		return False

	# create a list of all common elements
	temp = []
	for e1 in L1:
		for e2 in L2:
			if e1 == e2:
				temp.append(e1)

	# removing duplicates
	intersection = []
	for elem in temp:
		if not(elem in temp):
			intersection.append(elem)

	return intersection