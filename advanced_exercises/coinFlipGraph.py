def flipPlot(min, max):
	'''
	Assumes min and max are positive integers and min < max
	this function plots a graph of heads against tails
	'''
	ratios = []
	diffs = []
	xAxis = []

	for flip in range(min, max + 1):
		xAxis.append(2**flip)

	for numFlip in xAxis: