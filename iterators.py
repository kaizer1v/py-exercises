'''
[video link](https://www.youtube.com/watch?v=jTYiNjvnHZY)

An `Iterable` object is a type of object or data structure
over which you can "iterate" through every element.

Example: A list in python is an `Iterable` object
'''

'''
# So, let's do this
l = [1, 2, 3]


print(dir(l))     # should have a `__iter__` method available
                  #   this means that this list is an `ietrable` object

# so let's iterate through it
print(l.next())   # will raise an Error, because list itself isn't an
                  #   iterator. Thus, we'll have to convert this list
                  #   into an iterator by doing

i = iter(l)       # `type(i)` will return `<class 'list_iterator'>`
                  #   We are just casting the list into an `iter` type

print(dir(i))     # since `i` is an iterator, it will have `__next__` method
'''


'''
So, using this concept, let's create an interable linked list
'''
from linked_list import Node

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

  def get_head(self):
    return self.head

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




# '''
# GENERATORS
# '''

from stacks import StackUsingArraysIterable

sua = StackUsingArraysIterable()
sua.push('a')
sua.push('b')
sua.push('c')
sua.push('d')
sua.push('e')


# a generator that yields one item from the stack at a time
def print_stack(s):
  while not s.is_empty():
    yield s.pop()

print('----------------------')
# print(next(print_stack(sua)))
# print(next(print_stack(sua)))
# print(next(print_stack(sua)))
# print(next(print_stack(sua)))


# Another way of looping through the stack is by
for node in sua:
  print(node)
