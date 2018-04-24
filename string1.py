#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# #printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
	# +++your code here+++
	c = ""
	if count < 10: c = count
	else: c = "many"
	return "Number of donuts: %s" % c


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
	# +++your code here+++
	str = ""
	if len(s) > 2:
		str = s[:2] + s[-2:]
	else:
		str = ''
	return str


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
	# +++your code here+++
	first_char = s[:1]
	new_str = ''
	for c in range(1, len(s)):
			if s[c] == first_char:
					new_str += '*'
			else:
					new_str += s[c]
	new_str = '%s%s' % (first_char, new_str)
	return new_str


# ======================================================== DO FROM HERE.

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
	# +++your code here+++
	new_a = a.replace(a[:2], b[:2], 1)
	new_b = b.replace(b[:2], a[:2], 1)
	return new_a +' '+ new_b




def isIn(char, aStr):
  '''
  char: a single character
  aStr: an alphabetized string (assumed to be sorted)
  
  returns: True if char is in aStr; False otherwise
  '''
  # Your code here
  if aStr == '':
    return False
  lb = 0
  ub = len(aStr)
  guess = (lb + ub) / 2
  if char == aStr[guess]:
      return True

  while len(aStr) > 1:
    if char < aStr[guess]:
      ub = guess
    elif char > aStr[guess]:
      lb = guess
    return isIn(char, aStr[lb: ub])

  return False




def lenRecur(aStr):
	'''
	aStr: a string

	returns: int, the length of aStr
	'''
	# Your code here
	if aStr == '':
		return 0
	length = 1
	if aStr[:-1] == '':
		return 1
	return length + lenRecur(aStr[:-1])



def lenIter(aStr):
	length = 0
	if aStr == '':
		return 0
	for char in aStr:
		length = length + 1

	return length



# Provided simple test() function used in main() to #print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	#print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
	#print 'donuts'
	# Each line calls donuts, compares its result to the expected for that call.
	test(donuts(4), 'Number of donuts: 4')
	test(donuts(9), 'Number of donuts: 9')
	test(donuts(10), 'Number of donuts: many')
	test(donuts(99), 'Number of donuts: many')

	#print
	#print 'both_ends'
	test(both_ends('spring'), 'spng')
	test(both_ends('Hello'), 'Helo')
	test(both_ends('a'), '')
	test(both_ends('xyz'), 'xyyz')

	
	#print
	#print 'fix_start'
	test(fix_start('babble'), 'ba**le')
	test(fix_start('aardvark'), 'a*rdv*rk')
	test(fix_start('google'), 'goo*le')
	test(fix_start('donut'), 'donut')

	#print
	#print 'mix_up'
	test(mix_up('mix', 'pod'), 'pox mid')
	test(mix_up('dog', 'dinner'), 'dig donner')
	test(mix_up('gnash', 'sport'), 'spash gnort')
	test(mix_up('pezzy', 'firm'), 'fizzy perm')



	#print
	#print 'lenIter'
	test(lenIter('mix e'), '4')
	test(mix_up('dog', 'dinner'), 'dig donner')
	test(mix_up('gnash', 'sport'), 'spash gnort')
	test(mix_up('pezzy', 'firm'), 'fizzy perm')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
