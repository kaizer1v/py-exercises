'''
Merge Sort

METHOD:


RUN TIME:
n•log(n)
'''
def merge_sort(l):

  def merge(a, b):
    aux = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
      if a[i] <= b [j]:
        aux.append(a[i])
        i += 1
      else:
        aux.append(b[j])
        j += 1
    if i == len(a):
      aux += b[j:]
    if j == len(b):
      aux += a[i:]
    return aux

  def sort(l):
    size = len(l)
    if size <= 1:
      return l

    mid = size // 2
    left = l[:mid]
    right = l[mid:]

    return merge(sort(left), sort(right))

  return sort(l)



print(merge_sort([5, 6, 9, 2, 4, 10, 8]))
print(merge_sort([5, 3, 9, 7, 2, 6]))
