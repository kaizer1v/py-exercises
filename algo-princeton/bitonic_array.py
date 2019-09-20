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

1. find the peak using binary search
2. perform binary search on left of peak
3. perform binary search on right of peak
'''

'''
returns peak element's index
'''
def find_peak(l):
  # validity check (requires at least 3 elements)
  if len(l) < 3:
    return max(l)

  low = 1
  high = len(l) - 1

  while low <= high:
    mid = (low + high) // 2

    left = l[mid - 1] if mid - 1 > 0 else float('-inf')
    right = l[mid + 1] if mid + 1 < len(l) else float('inf')

    if left < l[mid] and right < l[mid]:
      return mid
    elif left > l[mid]:
      high = mid - 1
    elif right > l[mid]:
      low = mid + 1
  return -1   # if not found

'''
modified binary search, where if you know
before hand, if the list is in ascending or descending
order, you can use that
'''
def binary_search(l, elem, asc):
  if len(l) == 1 and l[0] != elem:
    return False

  mid = len(l) // 2
  if l[mid] == elem:
    return True

  if elem > l[mid]:
    new_l = l[mid + 1:] if asc == True else l[:mid]
  else:
    new_l = l[:mid] if asc == True else l[mid + 1:]

  return binary_search(new_l, elem, asc)

def bitonic_search(l, elem):
  peak_ind = find_peak(l)

  if elem == l[peak_ind]:
    return True
  
  return binary_search(l[:peak_ind], elem, True) or binary_search(l[peak_ind + 1:], elem, False)



sample_l = [1, 2, 3, 2, 1, -2]
# sample_l = [1, 2, 3, 4, 1]
# sample_l = [1, 6, 5, 4, 3]
# print(bitonic_search(sample_l))

print(bitonic_search([1, 2, 3, 4, 5, 6, 0, -4, -8], -8))
