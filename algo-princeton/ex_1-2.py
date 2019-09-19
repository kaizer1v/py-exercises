#!/usr/bin/python3.6

##############################################
## Module 1 - Session 2: BUILT-IN DATA TYPES
##############################################


## -----
## NOTES
## -----

'''

* float('inf') for positive infinity

* float('-inf') for negative infinity

* `-0.0/3.0` will give you a `-0.0`

* 0.1 + 0.1 + 0.1 == 0.3 will evaluate to False because of floating point precisions
    the precision of floating point numbers is upto 15 digits (Check IEEE 754 standards)

* doing a `round(0.5)` will return an interger value in Python3 in this case
    `round(0.5)`          will return 0
    `round(0.500000001)`  will return 1

* `3.0 == 3` will return True. Python will automatically conver the integer into a
    float i.e. in this case from 3 to 3.0 and then do the comparison

* You can compare multiple variables like
    `4 < 5 < 6` will evaluate to True

* Similarily, you can also assign multiple variables to the same value
    `a = b = c = 5`

* `(False - True - True) * True` will evaluate to -2


Q: What happens if I access a variable that I haven't bound to an object?
A: `NameError`

Q: How can you determine the type, representation and identify of a value?
A: `type()`, `repr()` and the `id()` method
  - `type()` - provides the data type. Eg: `type(False)` returns `<class 'bool'>`
  - `repr()` - provides the string representation. Eg: `repr({'a': 123})` returns
                "{'a': 123}"
  - `id()` - provides 

'''





## ---------
## EXERCISES
## ---------


''' 00
Take command line arguments from python
'''
import sys

def cmdArgs():
  # the args that you will receive will always be a string
  print('your first argument is = ', sys.argv[1])
  print(type(sys.argv[1]))
  print('is it False?', sys.argv[1] == False)

# cmdArgs()


'''01
writes a proper sentence with the names in the reverse of the order they are given, so that, for example, python
`usethree.py Alice Bob Carol` writes the string 'Hi Carol, Bob, and Alice'
'''
def usethree():
  # check out more formatting options here (https://pyformat.info/)
  sent = 'Hi {:s}, {:s} and {:s}'
  print(sent.format(sys.argv[3], sys.argv[2], sys.argv[1]))

usethree()



''' 01
Continuously compounded interest. Compose a program that calculates and writes the
amount of money you would have if you invested it at a given interest rate compounded
continuously, taking the number of years t, the principal P, and the annual interest
rate r as commmand-line arguments. The desired value is given by the formula p*e ** (r*t).
'''
def cci(time, P, r, n=1):
    e = 2.7183
    return P * ((1 + (r/100) / n) ** (r*time))

# print(cci(2, 10000, 15))


''' 011
Take three numbers and sort them in ascending order
'''
def threeSort(a, b, c):
    minimum = min([a, b, c])
    maximum = max([a, b, c])
    middle = a + b + c - minimum - maximum
    return [minimum, middle, maximum]

# print(threeSort(5, 7, 1))
