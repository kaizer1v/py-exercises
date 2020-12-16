'''
Social network connectivity.

Given a social network containing `n` members and a log file
containing `m` timestamps at which times pairs of members formed friendships,
design an algorithm to determine the earliest time at which all members areconnected
(i.e., every member is a friend of a friend of a friend ... of a friend).

Assume that the log file is sorted by timestamp and that friendship is an
equivalence relation. The running time of your algorithm should be
`mlogn` or better and use extra space proportional to `n`.
'''
class Network:

  garph = []
  weight = []

  def friend(self, a, b):
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

  def root(self, a):
    while a != self.graph[a]:
      self.graph[a] = self.graph[self.graph[a]]
      a = self.graph[a]
    return a

  def connected(self, a, b):
    return self.root(a) == self.root(b)

  def all_connected(self):
    pass

  def __init__(self, size):
    self.graph = [i for i in range(size)]
    self.weight = [i for i in range(size)]


# log file entries
network = Network(10)

network.friend(3, 4)
network.friend(4, 8)
network.friend(3, 8)
network.friend(5, 6)
network.friend(1, 2)
network.friend(5, 0)

print(network.all_connected(), network.sets)
