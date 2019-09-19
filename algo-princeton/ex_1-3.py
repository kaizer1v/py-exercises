##############################################
## Module 1 - Session 3: CONDITIONALS & LOOPS
##############################################


## ---------
## EXERCISES
## ---------

'''
takes three integer command-line arguments and writes 'equal' if all three are
equal, and 'not equal' otherwise
'''
def threeEqual():




'''
reverse a list
'''
def reverse(l):
    n = len(l)
    for i in range(n // 2):
        l[i], l[n - i - 1] = l[n - i - 1], l[i]
    return l

# print(reverse([1]))
# print(reverse([1, 2, 3]))
# print(reverse([1, 2, 3, 4]))




'''
create a 2D array
'''
def create2D(rowCount, colCount, value=None):
    '''
    Create and return a 2D array having rowCount rows and colCount
    columns, with each element initialized to value.
    '''
    a = [None] * rowCount
    for row in range(rowCount):
      a[row] = [value] * colCount
    return a

# print(create2D(3, 3, 0))



def write2D(a):
    """
    Write two-dimensional array a to sys.stdout.  First write its
    dimensions. bool objects are written as 0 and 1, not False and True.
    """
    rowCount = len(a)
    colCount = len(a[0])
    print(str(rowCount) + ' ' + str(colCount))
    for row in range(rowCount):
        for col in range(colCount):
            #stdio.writef('%9.5f ', a[row][col])
            element = a[row][col]
            if isinstance(element, bool):
                if element == True:
                    print(1)
                else:
                    print(0)
            else:
                print(element)
            print(' ')
        print()

# write2D(create2D(3, 3, 0))




'''
longest plateau
'''
def longestStreak(arr):
    i = 0
    n = len(arr)
    if n <= 1:
        return 1
    prev = arr[0]
    longest, count = 1, 1

    for i in range(1, n):
        if arr[i] == prev:                           # you are in a pleatue
            count += 1
            if count > longest:                      # count how big the plateau is
                longest = count
        else:
            count = 1
        prev = arr[i]

    return longest

# print(longestStreak([1]))
# print(longestStreak([1, 1]))
# print(longestStreak([1, 1, 2, 2]))
# print(longestStreak(['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']))




import random
class PlayingCards:

    suits = ['clubs', 'spades', 'diamonds', 'hearts']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck  = []

    for s in suits:
        for r in ranks:
            deck += [r + ' of ' + s]

    def shuffle(self):
        # shuffles the deck
        n = len(self.deck) - 1
        for i in range(n):
            r = random.randrange(0, n)
            temp = self.deck[r]
            self.deck[r] = self.deck[i]
            self.deck[i] = temp
        return self.deck

    def drawSpecific(self, ind):
        if not ind in range(0, 52):
            return False
        return self.deck[ind]

    def drawRandom(self):
        # draw a random card (repeats)
        r = random.randrange(0, len(self.deck))
        return self.deck[r]

pc = PlayingCards()
print(pc.shuffle())













