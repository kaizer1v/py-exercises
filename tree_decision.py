'''
Exploring the Knapsack Problem:
This basically states, given a set of characteristics
of some objects (like, weight and value), we need to 
get a set of limited objects whose sum of the weights
lies within a given constraint, but should have max
value.
'''

from tree_binary import *

## make a decision tree
## for efficiency should really generate on the fly, but here will build
## and then search

def buildDTree(sofar, todo):
	'''
	sofar and todo are 2 lists. Given those,
	construct a decision tree. This function
	will basically generate a tree including
	all possibilities of combinations of the nodes.
	So, at the end, the leaves will basically be 
	all the subsets that are possible for the 
	given set.
	'''
  if len(todo) == 0:
    return binaryTree(sofar)
  else:
    withelt = buildDTree(sofar + [todo[0]], todo[1:])
    withoutelt = buildDTree(sofar, todo[1:])
    here = binaryTree(sofar)
    here.setLeftBranch(withelt)
    here.setRightBranch(withoutelt)
    return here



# [value, weight]
a = [6, 3]
b = [7, 2]
c = [8, 4]
d = [9, 5]

# using the above value, weight pairs, we need
#   to generate a decision tree. This will create
#   all the possible subsets of the sets. 
treeTest = buildDTree([], [a, b, c, d])





# Now that we have a decision tree, using the
#   value, weight pairs and some constraints 
#   lets create using DFS the best combinations
#   using those constraints.

# Here are some constraints
def sumValues(lst):
  vals = [e[0] for e in lst]
  return sum(vals)

def sumWeights(lst):
  wts = [e[1] for e in lst]
  return sum(wts)

def WeightsBelow10(lst):
  return sumWeights(lst) <= 10

def WeightsBelow6(lst):
  return sumWeights(lst) <= 6




# Here is the DFS on Decision Tree
def DFSDTree(root, valueFcn, constraintFcn):
  stack = [root]
  best = None
  visited = 0
  while len(stack) > 0:
    
    visited += 1
    if constraintFcn(stack[0].getValue()):

      if best == None:
        best = stack[0]
        #print best.getValue()
      elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
        best = stack[0]
        #print best.getValue()

	    temp = stack.pop(0)
	    if temp.getRightBranch():
        stack.insert(0, temp.getRightBranch())
	    if temp.getLeftBranch():
        stack.insert(0, temp.getLeftBranch())
    
    else:
      stack.pop(0)
  
  #print 'visited', visited
  return best


# lets do the same using BFS on Decision Trees
def BFSDTree(root, valueFcn, constraintFcn):
  queue = [root]
  best = None
  visited = 0
  while len(queue) > 0:

    visited += 1
    if constraintFcn(queue[0].getValue()):

      if best == None:
        best = queue[0]
        #print best.getValue()
      elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
        best = queue[0]
        #print best.getValue()
       
      temp = queue.pop(0)
      if temp.getLeftBranch():
        queue.append(temp.getLeftBranch())
      if temp.getRightBranch():
        queue.append(temp.getRightBranch())
    
    else:
      queue.pop(0)
  
  #print 'visited', visited
  return best



# using the constraints and generating best possible
#   combinations of pairs based on given constraints.
#   Here, we need the max sum with weights <= 10
#print ''
#print 'DFS decision tree'
foobar = DFSDTree(treeTest, sumValues, WeightsBelow10)
#print foobar.getValue()

#print ''
#print 'BFS decision tree'
foobarnew = BFSDTree(treeTest, sumValues, WeightsBelow10)
#print foobarnew.getValue()






def DFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
  stack = [root]
  best = None
  visited = 0
  while len(stack) > 0:
    visited += 1
    
    if constraintFcn(stack[0].getValue()):

      if best == None:
        best = stack[0]
        #print best.getValue()
      elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
        best = stack[0]
        #print best.getValue()
      if stopFcn(best.getValue()):
        #print 'visited', visited
        return best
        
      temp = stack.pop(0)
      if temp.getRightBranch():
        stack.insert(0, temp.getRightBranch())
      if temp.getLeftBranch():
        stack.insert(0, temp.getLeftBranch())
  
    else:
      stack.pop(0)
  #print 'visited', visited
  return best

def BFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
  queue = [root]
  best = None
  visited = 0
  while len(queue) > 0:
      
    visited += 1
    if constraintFcn(queue[0].getValue()):
      if best == None:
        best = queue[0]
        #print best.getValue()
      elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
        best = queue[0]
        #print best.getValue()
      if stopFcn(best.getValue()):
        #print 'visited', visited
        return best
      
      temp = queue.pop(0)
      if temp.getLeftBranch():
        queue.append(temp.getLeftBranch())
      if temp.getRightBranch():
        queue.append(temp.getRightBranch())
    else:
        queue.pop(0)
  
  #print 'visited', visited
  return best

def atLeast15(lst):
  return sumValues(lst) >= 15

#print ''
#print 'DFS decision tree good enough'
foobar = DFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10, atLeast15)
#print foobar.getValue()

#print ''
#print 'BFS decision tree good enough'
foobarnew = BFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10, atLeast15)
#print foobarnew.getValue()