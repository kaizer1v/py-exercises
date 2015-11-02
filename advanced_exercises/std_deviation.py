def standardDeviation(lst):
	'''
	For a given list of numbers,
	this function plots the standard
	deviation of the numbers.
	'''
	mean = statisticalMean(lst)
	total = 0.0
	for item in lst:
		total += (item - mean)**2

	return (total/len(lst))**0.5


sample = [1, 4.3, 2.7, 6.3, 9, 5.5]
print standardDeviation(sample)



def statisticalMean(lst):
	'''
	For a given list of numbers,
	returns statistical mean of
	all numbers.
	'''
	return float(sum(lst)) / len(lst)