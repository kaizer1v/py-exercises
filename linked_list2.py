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
