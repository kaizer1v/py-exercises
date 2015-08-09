def inversions(L):
	'''
	Let A[1...n] be an array of distinct numbers. If i < j and A[i] > A[j], then
	the pair (i, j) is called an inversion of A.
	'''

	i = 0
	inversions = []
	while i < len(L) - 1:
		j = i + 1
		while j < len(L):
			if L[j] < L[i]:
				inversions.append((i, j))
			j += 1
		i += 1

	return inversions