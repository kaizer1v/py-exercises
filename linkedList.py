'''
Single Linked List
- new element is inserted at the head
'''

class SingleLinkedList:

    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = self._Node('HEAD')
        self.tail = self._Node('TAIL')
        self.head.next = self.tail
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

    def is_empty(self):
        return self.size == 0

    def insert(self, value):
        n = self._Node(value)
        n.next = self.head.next
        self.head.next = n
        self.size += 1
        return self

    def remove(self, value):
        pass
