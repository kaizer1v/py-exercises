def longestSubstr():
	"""
	Given a long string, we need to find the longest substring where all the letters in
	increasing order
	"""

	s = 'feeagrepoasdgrepasdjrepgassbrebgaspdodge'
	alphabets = 'abcdefghijklmnopqrstuvwxyz'
	substr = s[0]
	longest = ''
	for i in range(1, len(s)):
		if alphabets.index(substr[-1:]) <= alphabets.index(s[i]):
	    substr += s[i]
		else:
	    if len(substr) > len(longest):
	      longest = substr
	    substr = s[i]

	# to check for the last series of characters
	if len(substr) > len(longest):
	  longest = substr
	    
	return longest