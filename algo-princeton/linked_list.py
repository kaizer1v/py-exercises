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

# node6 = Node(6)
# node3 = Node(3)
# node4 = Node(4)
# node2 = Node(2)
# node1 = Node(1)

# node6.set_next(node3)
# node3.set_next(node4)
# node4.set_next(node2)
# node2.set_next(node1)


'''
practice problem - given a head node, return
the size the linked list
'''
def countNodes(head):
  if head.get_next() == None:
    return 1

  next_node = head.get_next()
  incr = 1
  while next_node != None:
    next_node = next_node.get_next()
    incr += 1

  return incr





class LinkedList:

  def insert(self, n_data):
    node = Node(n_data, self.head)
    self.head = node

  def remove(self, n_data):
    pass

  def find(self, n_data):
    node = self.head
    while node.get_next() != None:
      if node.get_data() == n_data:
        return True
      node = node.get_next()
    return node.get_data() == n_data

  def print(self):
    node = self.head
    while node.get_next() != None:
      print(node.get_data())
      node = node.get_next()
    if node.get_next() == None:
      print(node.get_data())

  def is_empty(self):
    return self.head == None

  def get_head(self):
    return self.head

  def __init__(self):
    self.head = None


# ll = LinkedList()
# ll.insert(6)
# ll.insert(3)
# ll.insert(4)
# print(ll.print())
# print(ll.find(4))
# ll.remove(3)
# ll.insert(2)
# ll.remove(6)
# ll.insert(1)
# print(ll.find(2))




'''
This is an iterable linked list
'''
class LinkedListIterable:

  def insert(self, n_data):
    node = Node(n_data, self.head)
    self.head = node

  def find(self, n_data):
    node = self.head
    while node.get_next() != None:
      if node.get_data() == n_data:
        return True
      node = node.get_next()
    return node.get_data() == n_data

  def print(self):
    node = self.head
    while node.get_next() != None:
      print(node.get_data())
      node = node.get_next()
    if node.get_next() == None:
      print(node.get_data())

  def is_empty(self):
    return self.head == None

  # NOTE: to make a data type iterable, you need to have this method
  def __iter__(self):
    return self

  # remove the 1st element from the linked list and return it
  def __next__(self):
    if self.head == None:
      raise StopIteration
    node = self.head
    self.head = node.get_next()
    return node.get_data()

  def __init__(self):
    self.head = None


lli = LinkedListIterable()
lli.insert(6)
lli.insert(4)
lli.insert(3)
lli.insert(1)
lli.insert(2)

# for elem in lli:
#   print('>>>>>', elem)


# you can even directly get the `next` elem
# print(next(lli))
# print(next(lli))
