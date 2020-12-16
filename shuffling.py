'''
Shuffling

[video link](https://www.coursera.org/learn/algorithms-part1/lecture/12vcF/shuffling)

This is a linear time shuffling algorithm

METHOD:
increment i, from 0 until the length of the list. At every increment, generate a
random number between 0 and i and then swap those two elements
'''
import random

def shuffling(l):
  for i in range(len(l) - 1):
    r = random.randint(0, i + 1)
    l[r], l[i] = l[i], l[r]
  return l

print(shuffling([1, 2, 3, 4, 5, 6]))
