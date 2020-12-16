'''
Stack implementation using a LinkedList
LIFO concept

+ insert & delete = O(1)
- search          = O(n)
'''

class Stack:

    class _Node:
        def __init__(self, elem, next=None):
            self._elem = elem
            self._next = next

        def __repr__(self):
            return '[' + str(self.elem) + ']->'

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        tr = ''
        p = self._head
        while p != None:
            tr += str(p._elem) + '\n'
            p = p._next
        return tr

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1
        return self

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._head._elem
  
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        to_return = self._head._elem
        self._head = self._head._next
        self._size -= 1
        return to_return
