def isPalindrome(str):
	"""
	This function checks for any given string
	whether it is a palindrome or not. If it is
	this returns true, false otherwise.

	TestCases:
		nitin
		abccba
		xyzyy
		keviv
	"""
	if len(str) % 2 == 0:
		mid = (len(str) / 2) - 1
	else:
		mid = len(str) / 2
	isPalindrome = True

	for i in range(0, mid + 1):
		if str[i] != str[-i-1]:
			isPalindrome = False
			break
	return isPalindrome

# Is there a faster way than this?, I guess yes
# TRY THIS
str = 'vtvtv'
if len(str) % 2 == 0:
    mid = (len(str) / 2) - 1
    print str[:mid+1] == str[mid:]
else:
    print 'there'
    mid = len(str) / 2
    print str[:mid] == str[mid+1:]



