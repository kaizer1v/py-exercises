'''
Week 1 - Ultra improved Quick Union

[video](https://www.coursera.org/learn/algorithms-part1/lecture/RZW72/quick-union-improvements)

In the weighted graph algorithm, when you look for a root of a node, you are
traversing through every node to get to the root - why not connect every node passed
through directly to the root? (will make traversing even faster)
This is called "Path Compression"
'''
class QU:

  garph = []
  weight = []

  def union(self, a, b):
    root_a = self.root(a)
    root_b = self.root(b)
    if root_a == root_b:
      return

    # check the weight of the trees
    if self.weight[a] < self.weight[b]:
      self.graph[root_a] = root_b
      self.weight[root_b] += self.weight[root_a]
    else:
      self.graph[root_b] = root_a
      self.weight[root_a] += self.weight[root_b]

  # -------------- LOOK HERE
  def root(self, a):
    while a != self.graph[a]:
      self.graph[a] = self.graph[self.graph[a]]
      a = self.graph[a]
    return a

  def connected(self, a, b):
    return self.root(a) == self.root(b)

  def __repr__(self):
    return str(self.graph)

  def __init__(self, size):
    self.graph = [i for i in range(size)]
    self.weight = [i for i in range(size)]



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
