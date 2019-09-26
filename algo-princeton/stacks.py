'''
this data structure uses linked lists
LIFO (Last In First Out)
-> [.., .., .., ..] |
'''
from linked_list import Node
from linked_list import LinkedList

class StackUsingLinkedLists:

  def is_empty(self):
    return self.head == None

  # pushes element as the first element
  def push(self, item):
    node = Node(item, self.head)
    self.head = node

  def pop(self):
    node = self.head
    self.head = self.head.get_next()
    return node

  def print(self):
    node = self.head
    while node.get_next() != None:
      print(node.get_data())
      node = node.get_next()
    if node.get_next() == None:
      print(node.get_data())

  def __init__(self):
    self.head = None


# sll = StackUsingLinkedLists()
# sll.push('a')
# sll.push('b')
# sll.pop()
# sll.push('c')
# sll.push('d')
# sll.pop()
# sll.pop()
# sll.push('e')
# print(sll.is_empty())
# sll.print()



class StackUsingArrays:

  def is_empty(self):
    return len(self.array) == 0

  def push(self, elem):
    self.array.append(elem)

  def pop(self):
    if self.is_empty():
      return -1
    popped = self.array[0]
    self.array = self.array[1:]
    return popped

  def print(self):
    print(list(self.array))

  def __init__(self):
    self.array = []


# sa = StackUsingArrays()
# sa.push('a')
# sa.push('b')
# sa.pop()
# sa.push('c')
# sa.push('d')
# sa.pop()
# sa.pop()
# sa.push('e')
# print(sa.is_empty())
# sa.print()


'''
when you append a new element in to a python array i.e. a list,
you are copying the whole array into a new array and then adding the new element
to be appeneded.


A `Dynamic Array` doubles the size of the array, when you add a new element to an 
already filled array.

Example of Dynamic Array

Say you have an existing array
l = [1, 2]

Now you append a new element
l.append(3)

A dynamic list will do this

new_l = [., ., ., .]    # size 4 (double of 2)

# copy all the elements from original array into the larger array
new_l[0] = l[0]
new_l[1] = l[1]

# and also add the new element
new_l[1] = 3

# so new_l becomes [1, 2, 3, .]

# re-assign the new to the old one
l = new_l
'''





class StackUsingArraysIterable:

  def is_empty(self):
    return len(self.array) == 0

  def push(self, elem):
    item = [elem]
    self.array = item + self.array

  def pop(self):
    if self.is_empty():
      return -1
    popped = self.array[0]
    self.array = self.array[1:]
    return popped

  def print(self):
    print(self.array)

  def __iter__(self):
    return self

  def __next__(self):
    if len(self.array) == 0:
      raise StopIteration
    ind = 0
    popped = self.pop()   # remove elements from top of stack (left most element in array)
    ind += 1
    return popped

  def __init__(self):
    self.array = []


suai = StackUsingArraysIterable()
suai.push(5)
suai.push(1)
suai.pop()
suai.push(6)
suai.push(2)
suai.pop()


# for elem in suai:
#   print(elem)
