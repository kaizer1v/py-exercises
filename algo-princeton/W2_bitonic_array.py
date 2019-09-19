'''
Search in a bitonic array. An array is bitonic if it is comprised of an
increasing sequence of integers followed immediately by a decreasing sequence
of integers. Write a program that, given a bitonic array of nn distinct integer
values, determines whether a given integer is in the array.

Best algo does it in ~2•lg(N) time
Average algo does it in ~3•lg(N) time
'''


'''
This is the algo for 3•lg(N) time

1. find the peak
2. perform binary search on left of peak
3. perform binary search on right of peak
'''
def find_peak_elem(l):
  # validity check
  if len(l) <= 2:
    print('here...')
    return max(l)

  mid = len(l) // 2
  peak = l[mid]

  # base condition
  if l[mid + 1] < peak and l[mid - 1] < peak:
    return peak

  if l[mid + 1] > peak:
    find_in = l[mid + 1:]
  else:
    find_in = l[:mid]

  return find_peak_elem(find_in)

def bitnoic_search(l, elem):
  pass

sample_l = [1, 2, 3, 2, 1, -2]
# sample_l = [1, 2, 3, 4, 1]
# sample_l = [1, 6, 5, 4, 3]
print(find_peak_elem(sample_l))
