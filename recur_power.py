def recurPower(base, exp):
	"""
	A function to calculate the exp'th power of base.

	base: int or float.
	exp: int >= 0
	----
	returns: int or float, base^exp
	"""
	if exp >= 0:
		if exp == 0:
			return 1
		return base * recurPower(base, exp - 1)



def recurPowerNew(base, exp):
	"""
	A function to calculate the exp'th power of base.
	But does an additional operation like so:
	when exp is even:
		base^exp = (base^2)^[exp/2]
	when exp is odd:
		base^exp = base * base^[exp - 1]
	when exp = 0:
		base^exp = 1

	base: int or float.
	exp: int >= 0
	----
	returns: int or float, base^exp
	"""

	if exp >= 0:
		if exp == 0:
			return 1
		elif exp % 2 == 0:
			# exp is an even integer
			return recurPowerNew(base*base, exp / 2)
		
		return base * recurPowerNew(base, exp - 1)