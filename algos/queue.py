'''
Queue

FIFO = First In First Out

[5] -> [7] -> [2] -> [3]
'''

from linked_list import Node

class QueueUsingLinkedList:

  # append a new item in the end
  def queue(self, item):
    node = Node(item, self.head)
    self.head = node

  # pop the first element inserted
  def dequeue(self):
    node = self.head
    while node.get_next().get_next() != None:
      node = node.get_next()

  def __init__(self):
    self.head = None



class QueueUsingArray:

  def is_empty(self):
    return len(self.array) == 0

  def queue(self, elem):
    self.array = [elem] + self.array

  def dequeue(self):
    if self.is_empty():
      return -1
    dq = self.array[-1]
    self.array = self.array[:-1]
    return dq

  def print(self):
    print(list(self.array))

  def __init__(self):
    self.array = []


qua = QueueUsingArray()
qua.queue(6)
qua.queue(4)
qua.print()
qua.queue(3)
qua.queue(1)
qua.queue(2)
qua.dequeue()
qua.print()

