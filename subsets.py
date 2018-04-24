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
    new.append(small+extra)
  
  #print 'smaller: ', smaller, 'extra: ', extra, 'new: ', new
  return smaller + new
    
# Example 1    
genSubsets([1, 2, 3])



def isSubset(L1, L2):
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
