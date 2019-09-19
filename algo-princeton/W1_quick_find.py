'''
Week 1 - Quick Find

a data structure that saves a connected
graph and has the functionality to tell whether
two points are connected by a line.

NOTE: this is a greedy algorithm, not necessarily the
best implementation.

How it works: watch this [video](https://www.coursera.org/learn/algorithms-part1/lecture/EcF3P/quick-find)
'''
class UF:
  graph = []

  '''
  given two points on a place `a` and `b`,
  connects them with a line.
  '''
  def union(self, a, b):
    if self.graph[b] == self.graph[a]:
      return True

    # store previous value at index `b`
    prev_b = self.graph[b]

    # connect b -> a
    # first change value at index `b` to value at index `a`
    self.graph[b] = self.graph[a]

    # now for all the previous value at index `b`, need to 
    #   be updated to the value at index `a`
    for i in range(len(self.graph)):
      if self.graph[i] == prev_b:
        self.graph[i] = self.graph[a]

    return True

  '''
  tells whether two points are connected
  by a line by `True` or `False`
  '''
  def connected(self, a, b):
    return self.graph[a] == self.graph[b]

  def __repr__(self):
    return str(self.graph)

  def __init__(self, size):
    self.graph = [i for i in range(size)]


import os

if __name__ == '__main__':
  input_file = open('inputs_union.txt', 'r')
  input_lines = input_file.readlines()

  size = int(input_lines[0])
  uf = UF(size)

  for i in range(1, len(input_lines)):
    inputs = list(map(int, input_lines[i].strip('\n').split(' ')))
    if uf.union(inputs[0], inputs[1]):
      print('Connecting {:d} & {:d}'.format(inputs[0], inputs[1]))

  print('Graph looks like', uf)
