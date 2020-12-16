'''
Selection sort

[video link](https://www.coursera.org/learn/algorithms-part1/lecture/VE0sv/selection-sort)

METHOD:
scan through all the elements, find the minimum and then put it with the 0th position
element and so on...

RUN TIME:
n + (n - 1) + (n - 2) + (n - 3) ...

n   - number of swaps
n^2 - number of comparisions (to find the min)
'''

def selection_sort(l):
  if len(l) <= 1:
    return l

  last_sorted = 0
  for i in range(len(l)):
    # 1. get min from the list
    min_i = find_min(l[i:])
    
    # 2. swap with the last sorted element
    l[last_sorted], l[last_sorted + min_i] = l[last_sorted + min_i], l[last_sorted]
    last_sorted += 1

  return l


# returns the index of the minimum value in the list
def find_min(l):
  length = len(l)
  if length <= 1:
    return 0

  m = l[0]
  mi = 0

  for ind in range(1, length):
    if l[ind] < m:
      m = l[ind]
      mi = ind

  return mi

