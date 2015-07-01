def biggest(aDict):
	'''
	aDict: A dictionary, where all the values are lists.

	returns: The key with the largest number of values associated with it
	'''
	# Your Code Here
	length = 0
	largest = ''
	if len(aDict) > 0:
		for item in aDict:
			if len(aDict[item]) >= length:
				length = len(aDict[item])
				largest = item
		return largest