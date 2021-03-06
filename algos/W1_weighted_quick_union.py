'''
Week 1 - mproved Quick Union

[video](https://www.coursera.org/learn/algorithms-part1/lecture/RZW72/quick-union-improvements)

Uses weighted graphs, where you weigh the graph, and attach the one which is smaller
to the larger one.

Always put the root of the smaller tree (by checking weight) under the root of the 
larger tree, this will increase the efficiency of "searching" for the root, since it
has to traverse less deep.

* Weight = number of nodes under a present node
NOTE: weight is NOT the depth of a tree
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
    #   and put smaller tree inside bigger tree
    if self.weight[a] < self.weight[b]:
      self.graph[root_b] = root_a
      self.weight[root_b] += self.weight[root_a]
    else:
      self.graph[root_a] = root_b
      self.weight[root_a] += self.weight[root_b]

  def root(self, a):
    if self.graph[a] == a:
      return a
    return self.root(self.graph[a])

  # this is just another way of writing the root function
  def root_loop(self, a):

    # until you find an `a` that's pointing to itself,
    #   keep checking for `a`'s parent
    while a != self.array[a]:
      a = self.array[a]
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
