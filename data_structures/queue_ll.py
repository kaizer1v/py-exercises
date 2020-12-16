'''
Queue implementation using a LinkedList
FIFO concept

+ insert & delete = O(1)
- search          = O(n)
'''

class Queue:

    class _Node:
        def __init__(self, e, next=None):
            self._elem = e
            self._next = next

        def __repr__(self):
            return '[{}]->'.format(str(self._elem))

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        tr = ''
        p = self._head
        while p != None:
            tr += '[' + str(p._elem) + ']->'
            p = p._next
        return tr

    def push(self, e):
        # push to begining
        n = self._Node(e, next=None)
        n._next = self._head
        self._head = n
        self._size += 1 
        return self

    def pop_b(self):
        # pop from beginning
        tr = self._head
        self._head = self._head._next
        self._size -= 1
        return tr

    def pop(self):
        # pop from end
        if self._size <= 1:
            return self._head._elem
        tr = ''
        p = self._head
        while p._next._next != None:
            p = p._next
        tr = p._next._elem
        p.
        return tr

    def is_empty():
        return self._size == 0

q = Queue()
q.push(5)
q.push(3)
q.push(9)

print(q)        # 9 -> 3 -> 5

q.pop()         # 5
print(q)        # 9 -> 3
