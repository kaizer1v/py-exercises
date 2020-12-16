# from linkedList import SingleLinkedList

# sll = SingleLinkedList()
# sll.insert(1).insert(3).insert(5).insert(9)
# print(len(sll))
# print(sll)


from stack import Stack

s = Stack()
s.push(5).push(10).push(3)      # 3 -> 10 -> 5
# print(s.pop())                  # 3
# s.push(8).push(4)               # 4 -> 8 -> 10 -> 5
# print(s.pop())                  # 4
# print(s)                        # [8] -> [10] -> [5]


for n in s:
    print(n)
