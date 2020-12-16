# Following should work
# L = Node(3) + Node(5) + Node(1)
# print(L)                  // [3] -> [5] -> [1] -> None

from stack_ll import Stack

L = Stack()
L.push(5).push(3).push(8)
print(L.pop())
L.push(9).push(4).push(7)
print(L.pop())
print('-------------------------------')
print(L)
print(L)
