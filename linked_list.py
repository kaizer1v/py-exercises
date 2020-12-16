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
Linked List
'''
class LinkedList(LinkedListExpectsNode):

  def insert(self, data):
    node = Node(data)
    LinkedListExpectsNode.insert(self, node)


ll = LinkedList()
ll.insert('e')
ll.insert('d')
ll.insert('a')
ll.insert('c')
ll.insert('b')
ll.print()

ll.remove('a')
ll.remove('f')    # doesn't exist
ll.print()


'''
Circular Linked List

the last element is linked to the first one
'''
class NodeSupportsCycle(Node):
  def __init__(self, data, last=False):
    self.last = last
    Node.__init__(self, data)


class CicrularLinkedList():

  def insert(self, data):
    node = NodeSupportsCycle(node, data)
    if not self.is_empty():
      node.set_next(self.head)
    else:
      node.last = True
    self.head = node

  def __init__(self):
    self.len = 0
    self.head = None
