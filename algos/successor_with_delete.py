'''
Successor with delete. Given a set of nn integers

S = { 0, 1, ... , n-1 }

and a sequence of requests of the following form:

* Remove `x` from S
* Find the successor of `x`, the smallest `y` in S such that y >= x

design a data type so that all operations (except construction) take
logarithmic time or better in the worst case.
'''
class SWD:
  lst = []

  def remove(self, x):
    ind = self.get_index_of(x)
    self.lst = self.lst[:ind] + self.lst[ind + 1:]

  def get_index_of(self, x):
    right = len(self.lst) - 1
    left = 0

    if right < 2:
      return 0

    while left <= right:
      mid = (left + right) // 2

      if self.lst[mid] == x:
        return mid
      elif x < self.lst[mid]:     # look on left
        right = mid - 1
      else:                       # look on right
        left = mid + 1

    return -1

  def find_successor(self, x):
    ind = get_index_of(x)
    if not ind == len(self.lst):    # if not the last index
      return self.lst[ind + 1]
    return None

  def __init__(self, size):
    self.lst = [i for i in range(size)]


swd = SWD(10)
swd.remove(6)
swd.remove(8)
print(swd.get_index_of(9))
