'''
It takes as input an array of numbers, and it
determines the contiguous subarray whose values have
the greatest sum. Here, this problem is interesting
only when there are negative numbers in the array,
else the max sub array would be the array itself.
'''

def maxSubArray(L, low, high):
	# low = 0
	# high = len(L)

	if high == 1 or low == high:
		return L

	mid = (low + high) / 2

	(leftLow, leftHigh, leftTotal) = maxSubArray(L, low, mid)
	(rightLow, rightHigh, rightTotal) = maxSubArray(L, mid + 1, high)
	(crossLow, crossHigh, crossTotal) = maxCrossingSubArray(L, low, mid, high)

	if leftTotal >= rightTotal and leftTotal >= crossTotal:
		return (leftLow, leftHigh, leftTotal)
	elif rightTotal >= leftTotal and rightTotal >= crossTotal:
		return (rightLow, rightHigh, rightTotal)
	else:
		return (crossLow, crossHigh, crossTotal)


def maxCrossingSubArray(L, low, mid, high):

# ====== left half 
	leftTotal = 0
	total = 0
	maxLeft = mid

	for i in range(mid, low - 1, -1):
		total += L[i]

		if total > leftTotal:
			leftTotal = total
			maxLeft = i

# ====== right half 
	rightTotal = 0
	total = 0
	maxRight = mid
	
	for j in range(mid + 1, high):
		total += L[j]
	
		if total > rightTotal:
			rightTotal = total
			maxRight = j

	return (maxLeft, maxRight, leftTotal + rightTotal)
