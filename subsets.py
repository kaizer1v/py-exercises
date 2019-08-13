def genSubsets(L):
    '''
    Given a list of integers. This function
    finds all the subsets that can be formed with
    these list elements. This returned object will
    be a list of (lists of subsets).
    '''
    res = []
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)

    # print 'smaller: ', smaller, 'extra: ', extra, 'new: ', new
    return smaller + new

# Example 1
print(genSubsets([1, 2, 3, 4, 5]))
print(genSubsets([1, 2, 3, 4]))
print(genSubsets([1, 2, 3]))

# The number of sets produced from a list would be = 2^n where n = length of the list
#   including an empty set as well as the list itself 


def countSubsets(L):
    '''
    given a list `L`, return the number
    of possible subsets
    '''
    return pow(2, len(L))


def isSubset(L1, L2):
    '''returns `True` if L1 is subset of L2, `False` otherwise'''
    s1 = set(L1)
    s2 = set(L2)
    return s1.issubset(s2)


def isSubsetOld(L1, L2):
    '''
    Assumes L1 and L2 are lists.
    Returns True if each element of L1 is also in L2
    and False otherwise.
    '''
    if len(L1) == 0 and len(L2) == 0:
        return False
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
