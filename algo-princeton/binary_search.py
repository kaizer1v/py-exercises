'''
given a sorted array, try and find a given value
'''

def binary_search(l, elem):
  if len(l) == 1 and l[0] != elem:
    return False

  mid = len(l) // 2
  if l[mid] == elem:
    return True

  if elem > l[mid]:
    # look on right-hand-side
    new_l = l[mid + 1:]
  else:
    # look on left-hand-side
    new_l = l[:mid]

  return binary_search(new_l, elem)


def binary_search_loop(l, elem):
  if len(l) == 1 and l[0] != elem:
    return False

  low = 0
  high = len(l) - 1

  while low <= high:
    mid = (low + high) // 2

    if l[mid] == elem:
      return True
    elif elem < l[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return False


'''
works if the list is in reverse order
'''
def binary_search_v2(l, elem, asc):
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


'''
In case of duplicates within a sorted (ascending) list,
return the item with the smallest index, for example
list    ->     [1, 2, 3, 3, 4]
indexes ->      0  1  2  3  4

incase of searching for element 3, return the index 2
'''

# cannot be recursive
def binary_search_with_duplicates(l, elem):
  if len(l) == 1 and l[0] != elem:
    return False

  low = 0
  high = len(l) - 1

  while low <= high:
    mid = (low + high) // 2

    if l[mid] == elem:
      if l[mid - 1] != elem:
        return mid
      else:
        i = mid
        while l[mid] == elem:
          i -= 1
        return i
    elif elem < l[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return False




sample_l = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
elem = 93

# print(binary_search(sample_l, elem))
print(binary_search_loop(sample_l, elem))
