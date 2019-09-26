'''
it is a data structure a list of nodes where every node in the list
points to the next node. The node can contain any kind of element like an integer
or a string or even objects
'''
class Node:

  def get_next(self):
    return self.next_node

  def set_next(self, node):
    self.next_node = node

  def get_data(self):
    return self.data

  def set_data(self, data):
    self.data = data

  def __init__(self, data, next_node=None):
    self.data = data
    self.next_node = next_node


class LinkedListExpectsNode:

  def is_empty(self):
    return self.head == None

  def insert(self, node):
    if not self.is_empty():
      node.set_next(self.head)
    self.head = node

  def remove(self, data):
    if self.is_empty():
      return None

    # if there's only one item
    if self.head.get_data() == data:
      self.head = self.head.get_next()
      return True

    node = self.head
    while node.get_next() != None:
      if node.get_next().get_data() == data:
        node.set_next(node.get_next().get_next())
        return True
      node = node.get_next()

    # last item
    if node.get_next() == None:
      if node.get_data() == data:
        self.head = None
        return True

    return False

  def find(self, data):
    if self.is_empty():
      return None

    node = self.head
    while node.get_next() != None:
      if node.get_data() == data:
        return True
      node = node.get_next()

    if node.get_next() == None:
      return node.get_data() == data

    return False

  def print(self):
    if self.is_empty():
      return 'Empty'

    node = self.head
    p = []
    while node.get_next() != None:
      p.append(node.get_data())
      node = node.get_next()
    p.append(node.get_data())
    print(' -> '.join(list(map(str, p))))

  def __init__(self):
    self.head = None

'''
Let's try to create a list of nodes like so
6 -> 3 -> 4 -> 2 -> 1
'''

# node6 = Node(6)
# node3 = Node(3)
# node4 = Node(4)
# node2 = Node(2)
# node1 = Node(1)

# ll = LinkedListExpectsNode()
# ll.insert(node6)
# ll.insert(node3)
# ll.insert(node4)
# ll.insert(node2)
# ll.insert(node1)

# print('2', ll.find(2))
# print('6', ll.find(6))
# print('4', ll.find(4))
# print('5', ll.find(5))

# ll.print()
# ll.remove(3)
# ll.print()



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


# lli = LinkedListIterable()
# lli.insert(6)
# lli.insert(4)
# lli.insert(3)
# lli.insert(1)
# lli.insert(2)

# for elem in lli:
#   print('>>>>>', elem)


# you can even directly get the `next` elem
# print(next(lli))
# print(next(lli))
