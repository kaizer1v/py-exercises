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
