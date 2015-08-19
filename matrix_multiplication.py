def isSqMatrix(A):
	'''
	returns True if the Matrix is a 
	square matrix i.e should be a n x n
	matrix, False otherwise.
	'''
	if type(A) == list and len(A) > 0:
		for elem in A:
			if type(elem) != list or len(elem) != len(A):
				return False
	else:
		return False
	return True

def matrixMult(A, B):
	'''
	Given two matrices of the same size
	returns the result of multiplication
	of two matrices.
	'''
	
	if isSqMatrix(A) == True and isSqMatrix(B) == True:
		if len(A) == len(B):
			result = []
			for i in range(0, len(A)):
				total = 0
				result[i].append([])
				print result
				for j in range(0, len(B)):
					total += A[i][j] * B[j][i]
					print (i, j), A[i][j], B[j][i]
				result[i][j] = total
				print total, result
				print



a = [[1, 2], [3, 4]]
b = [[7, 4], [2, 6]]
matrixMult(a, b)



# Testing isSqMatrix
print 'a', isSqMatrix([[1, 2], [3, 4]]),                    # True
print 'b', isSqMatrix([]),                                  # False
print 'c', isSqMatrix([1, 2, 4]),                           # False
print 'd', isSqMatrix([[[]]]),                              # True | should be False
print 'e', isSqMatrix([[1, 4, 4], [2, 45]]),                # False
print 'f', isSqMatrix([[1, 3], 4]),                         # False
print 'g', isSqMatrix([[44], [5], [3]]),                    # False
print 'h', isSqMatrix([[1]]),                               # True
print 'i', isSqMatrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])    # True




def initializeMatrix(n, m):
	'''
	Defines a n x m matrix where
	n = number of rows
	m = number of columns
	'''
	return [[0 for x in range(m)] for x in range(n)]

def initializeSqMatrix(n):
	'''
	Defines a square matrix of size n x n
	'''
	return [[0 for x in range(n)] for x in range(n)]


def matrixMultRecur(A, B):

	C = initializeMatrix(2, 2)
	c[0][0] = matrixMultRecur(A[0][0], B[0][0]) + matrixMultRecur(A[0][1], B[1][0])