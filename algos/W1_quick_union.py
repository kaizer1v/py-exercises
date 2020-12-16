'''
Week 1 - Quick Union

[video](https://www.coursera.org/learn/algorithms-part1/lecture/ZgecU/quick-union)

Uses a lazy appraoch to store the elements. So, every element in the list
becomes the parent of the index at that element. (essentially building a tree)

--> indexes    0  1  2  3  4  5  6  7  8  9
--> array     [0, 1, 9, 4, 9, 6, 6, 7, 8, 9]

Looking at this array, the parent of
- 0 is 0
- 2 is 9
- 3 is 4
etc.
'''
class QU:

  garph = []

  def union(self, a, b):
    i = self.root(a)
    j = self.root(b)
    self.graph[i] = j
    return True

  def root(self, a):
    if self.graph[a] == a:
      return a
    return self.root(self.graph[a])

  def connected(self, a, b):
    return self.root(a) == self.root(b)

  def __repr__(self):
    return str(self.graph)

  def __init__(self, size):
    self.graph = [i for i in range(size)]



size = 10
qu = QU(size)

qu.union(4, 3)
qu.union(3, 8)
qu.union(6, 5)
qu.union(9, 4)
qu.union(2, 1)

print(qu.connected(8, 9))    # True
print(qu.connected(5, 4))    # False

qu.union(5, 0)
qu.union(7, 2)
qu.union(6, 1)
qu.union(7, 3)

print(qu.graph)
