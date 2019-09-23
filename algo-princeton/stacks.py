'''
this data structure uses linked lists
'''
class StackUsingLinkedLists:

  def is_empty(self):
    pass

  def push(self, item):
    pass

  def pop(self):
    pass

  def __init__():
    pass



class StackUsingArrays:

  def is_empty(self):
    return self.size == 0

  def push(self, elem):
    if (self.size + 1) > len(self.array):
      return False

    self.size += 1
    self.array[size] = elem
    return True

  def pop(self):
    if (self.size - 1) < 0:
      return False

    self.size -= 1
    popped_item = self.array[size]
    self.array[size] = None
    return popped_item

  def __init__(self, size=10):
    self.array = [None for i in range(size)]
    self.size = size
