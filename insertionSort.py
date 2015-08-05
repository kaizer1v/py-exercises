def insertionSort(L):
  '''
  Given a card, sort it within the given
  already sorted list.
  '''

  for i in range(1, len(L)):
    currNumber = L[i]

    # run backwards from 1 less than the current index, until 0
    j = i - 1
    while j >= 0:

      # if I find a number which is greater than the current number,
      #   move it 1 step up
      if L[j] > currNumber:
        L[j + 1] = L[j]
      else:
        break
      j -= 1

    # since you have already decremented j by 1, and checked
    #   it against the left element, we need to add 1 and put the
    #   current element there. We are at this line because, the check 'L[j] > currNumber'
    #   did not satisfy, thus, it then went to the line ' j -= 1 ', so we need to add 1
    #   again
    L[j + 1] = currNumber

x = [5, 2, 4, 6, 1, 3]
insertionSort(x)
print x




def insertionSort2(L, fn):
  '''
  apart from the fact that this sorting has more swapping
  than the previous one, it also starts the comparison of 
  every new element against the already sorted part from 
  left to right, instead of the right to left.
  '''

  for i in range(1, len(L)):
    currNumber = L[i]
    
    j = 0
    while j < i:

      if fn(L[j], currNumber) == True:
        L[j], L[i] = L[i], L[j]

      j += 1


'''
These are helper functions, that you can 
pass to the insertionSort2 function to either
sort it in ascending or descending order.
'''
def asc(x, y):
  if x > y:
    return True
  return False

def desc(x, y):
  if x < y:
    return True
  return False



x = [31, 41, 59, 26, 41, 58]
insertionSort2(x, desc)
print x