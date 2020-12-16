'''
Permutation. Given two integer arrays of size nn, design a subquadratic algorithm
to determine whether one is a permutation of the other. That is, do they contain
exactly the same entries but, possibly, in a different order.
'''
def is_permutation(a, b):
  if len(a) != len(b):
    return False

  for i in range(len(a)):
    if a[i] not in b:
      return False
  return True


print(is_permutation([1, 4, 2, 5], [5, 2, 4, 1]))   # True
print(is_permutation([1, 4, 2, 5], [5, 2, 1, 8]))   # False



'''
Dutch National Flag.

Given an array of `n` buckets, each containing a 
red, white, or blue pebble, sort them by color.

The allowed operations are:

* `swap(i, j)`: swap the pebble in bucket `i` with the pebble in bucket `j`
* `color(i)`  : determine the color of the pebble in bucket `i`

The performance requirements are as follows:

* At most `n` calls to color()
* At most `n` calls to swap()
* Constant extra space
'''
def dutch_national_flag(l):
  order = {
    'red': 1,
    'white': 2,
    'blue': 3
  }

  
