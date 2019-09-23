'''
it is a data structure a list of nodes where every node in the list
points to the next node. The node can contain any kind of element like an integer
or a string or even objects
'''
class Node:

  def get_data(self):
    return self.data

  def set_data(self, data):
    self.data = data

  def get_next(self):
    return self.next_node

  def set_next(self, node):
    self.next_node = node

  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node

'''
Let's try to create a list of nodes like so
6 -> 3 -> 4 -> 2 -> 1
'''

node6 = Node(6)
node3 = Node(3)
node4 = Node(4)
node2 = Node(2)
node1 = Node(1)

node6.set_next(node3)
node3.set_next(node4)
node4.set_next(node2)
node2.set_next(node1)



# class LinkedList:

#   # will add a node to the beginning of the linked list
#   def insert(self, data):           # currently the linked list looks like        * -> z -> y -> ... -> None
#     new_node = Node(data, None)     # 1. create a new node with given data        d -> None
#     new_node.set_next(self.head)    # 2. point new node to current head           d -> z
#     self.head = new_node            # 3. make the head pointer point to new node  * -> d -> z -> x -> ... -> None
#     self.size += 1

#   # look for a node with a particular data
#   def find(self, data):

#     while 

#   # remove a specified node from the list
#   def remove(self, node):
#     pass

#   def get_size(self):
#     return size 

#   def __init__(self):
#     self.head = None
#     self.size = 0
