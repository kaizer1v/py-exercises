from tree_decision import *


def DTImplicit(toConsider, avail):
  if toConsider == [] or avail == 0:
    result = (0, ())
 
  elif toConsider[0][1] > avail:
    result = DTImplicit(toConsider[1:], avail)
  
  else:
    nextItem = toConsider[0]
    withVal, withToTake = DTImplicit(toConsider[1:], avail - nextItem[1])
    withVal += nextItem[0]
    withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
    
    if withVal > withoutVal:
      result = (withVal, withToTake + (nextItem,))
    else:
      result = (withoutVal, withoutToTake)
  
  return result

stuff = [a,b,c,d]

val, taken = DTImplicit(stuff, 10)

#print ''
#print 'implicit decision search'
#print 'value of stuff'
#print val
#print 'actual stuff'
#print taken