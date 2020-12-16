'''
Write a program that, given an array a[] of n distinct integers, finds a
local minimum: an index i such that both

a[i] < a[i-1] and a[i] < a[i+1]

(assuming the neighboring entry is in bounds). Your program should use
~ 2 lg n
compares in the worst case.
'''

# O(n - 2)
def local_min_v1(l):
  lm = 0
  for i in range(1, len(l) - 1):
    if l[i - 1] < l[i] and l[i + 1] < l[i]:
      # lm = l[i]
      return l[i]
  return lm


def local_min_v2(l):
  if len(l) < 3:
    return

  p = len(l) // 2

  while p >= 1 and p < len(l) - 1:
    if l[p - 1] < l[p] and l[p + 1] < l[p]:
      return [p, l[p]]

    if l[p + 1] > l[p]:
      # move pointer to right
      p = p + 1
    elif l[p - 1] > l[p]:
      # move left
      p = p - 1

  return False


# O(2•lg(n))
'''
Examine the middle value a[n/2] and its two neighbors a[n/2 - 1] and a[n/2 + 1].
If a[n/2] is a local minimum, stop; otherwise search in the half with the
bigger neighbor.

NOTE: this would work only when the list is in a sorted order
'''
def local_min_v3(l):
  low = 1
  high = len(l) - 2

  if len(l) < 3:
    return None

  while low <= high:
    mid = (low + high) // 2

    if (l[mid - 1] < l[mid]) and (l[mid + 1] < l[mid]):
      return l[mid]

    if l[mid - 1] > l[mid]:
      high = mid - 1
    elif l[mid + 1] > l[mid]:
      low = mid + 1

  return -1



# sample_l = [1, 2]                     # None
# sample_l = [1, 3, 2]                  # 3
sample_l = [11, 10, 8, 16, 13, 22]
# print(local_min_v1(sample_l))
print(local_min_v3(sample_l))
