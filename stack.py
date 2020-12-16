'''
Stack using a linked list
LIFO: Last In First Out
'''
class Stack:

    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = self._Node('HEAD')
        self.tail = self._Node('TAIL')
        self.head.next = self.tail
        self.cursor = self.head
        self.size = 0

    def __repr__(self):
        cursor = self.head.next
        to_return = '|-[{}]->'.format(str(self.head.value))
        while cursor.next != None:
            to_return += '['+ str(cursor.value) +']->'
            cursor = cursor.next
        return to_return + '[{}]-|'.format(str(self.tail.value))

    def __len__(self):
        return self.size

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor.next == self.tail.value:
            raise StopIteration
        else:
            to_return = self.cursor.value
            self.cursor = self.cursor.next
            return to_return
        
    def push(self, value):
        n = self._Node(value)
        n.next = self.head.next
        self.head.next = n
        self.size += 1
        return self

    def pop(self):
        if not self.is_empty():
            to_return = self.head.next
            self.head.next = self.head.next.next
            self.size -= 1
            return to_return.value
        else:
            raise Exception('Stack is Empty')

    def is_empty(self):
        return self.size == 0
