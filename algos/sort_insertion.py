'''
Insertion Sort

[video link](https://www.coursera.org/learn/algorithms-part1/lecture/1hYlN/insertion-sort)

METHOD:
starting from the left most, sort all the elements until your current element. For
example, if you are at the 3rd element, everything to the left of it would be sorted
by moving one position to the left, comparing it with that element, if smaller
then swapping it.

RUN TIME:

'''

def insertion_sort(l):
  last = len(l) + 1       # why + 1? A: to sort the last element as well
  for i in range(1, last):
    l[:i] = backward_sorting(l[:i])
  return l

def backward_sorting(l):
  # for a given the last element
  #   put it in the right place until 0
  if len(l) <= 1:
    return l

  j = len(l) - 1
  while j >= 1:
    if l[j] < l[j - 1]:
      l[j], l[j - 1] = l[j - 1], l[j]
    else:
      return l
    j -= 1

  return l


print(insertion_sort([9, 1, 4, 7, 8, 6]))
