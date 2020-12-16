class BinaryTree(object):

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

	def setLeftBranch(self, node):
		self.left = node

	def setRightBranch(self, node):
		self.right = node

	def setParent(self, node):
		self.parent = node

	def getLeftBranch(self):
		return self.left

	def getRightBranch(self):
		return self.right

	def getParent(self):
		return self.parent

	def getValue(self):
		return self.value

	def __str__(self):
		return self.value

# Now, lets build a binary tree :)

'''
			(5)
		   /   \
		 (2)    (8)
        /   \\  / 
      (1)  (4) (6)
           /     \\ 
		  (3)	 (7)

''' 


n5 = binaryTree(5)		# root node
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)

# Now that we have created a tree, let us try to use this tree
# We can primarily use this tree to let's say; find an element within it
# There are 2 ways of doing this, breadth first search or depth first search


def DFSBinary(root, fcn):
	'''
	Given a node value, and a tree within which
	you want to search this node, use depth first
	algorithm to find the node. If it exists,
	return True; False otherwise.
	'''
	stack = [root]
	while len(stack) > 0:
		#print 'at node ' + str(stack[0].getValue())
		if fcn(stack[0]):
			return True
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
	return False


# these are some helper functions that we will pass in DFSBinary
def find6(node):
	return node.getValue() == 6

def find10(node):
	return node.getValue() == 10

def find2(node):
	return node.getValue() == 2

def gt6(node):
	return node.getValue() > 6

# lets try and find 6 within the generated binary tree
#print DFSBinary(n5, find6)

# lets try finding something that doesn't exist in the BinaryTree
#print DFSBinary(n5, find10)


# Similar to this is the Breadth First Binary tree algorithm, 
# but in this case we will be using a queue data-structure.

def BFSBinary(root, fcn):
	'''
	Given a node value, and a tree within which
	you want to search this node, use breadth first
	algorithm to find the node. If it exists,
	return True; False otherwise.
	'''
	queue = [root]
	while len(queue) > 0:
		#print 'at node ' + str(queue[0].getValue())
		if fcn(queue[0]):
			return True
		else:
			temp = queue.pop(queue[0])
			if temp.getRightBranch():
				queue.append(temp.getRightBranch())
			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch())
	return False



	# Let us also keep track of the path we are following
	#		within the binary tree while searching.

def DFSBinaryPath(root, fcn):
	'''
	Given a node value, and a tree within which
	you want to search this node, use breadth first
	algorithm to find the node. If it exists,
	then return the path you took to find the node.
	'''
	stack = [root]
	while len(stack) > 0:
		if fcn(stack[0]):
			return TracePath(stack[0])
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
	return False

def TracePath(node):
	'''
	Returns the path to this node, until you
	reach the root node, from bottom up.
	'''
	if not node.getParent():
		return [node]
	else:
		return [node] + TracePath(node.getParent())


#print''
#print 'DFS path'
pathTo6 = DFSBinaryPath(n5, find6)
#print [e.getValue() for e in pathTo6]



# But, we can still optimize the searching for particular element
# 	further, by knowing that in an ordered binary tree, all the elements
#		lt the current node will lie on the left and gt the current node will
#		lie on the right branch. Thus,

def DFSBinaryOrdered(root, fcn, ltFcn):
	'''
	For a given Ordered Binary Tree, find a node
	using fcn and return True, if it exists, else
	return False
	'''
	stack = [root]
	while len(stack) > 0:
		if fcn(stack[0]):
			return True
		elif ltFcn(stack[0]):
			temp = stack.pop(0)
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
		else:
			temp = stack.pop(0)
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
	return False
