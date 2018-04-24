'''
Every tree starts from a parent, called as the parent Node.
Every node, has a left node and a right node, they are the parent's children.
All the nodes at the same level are called as siblings.
'''

class Node(object):
	'''
	A node is an element of a tree, it has it's own
	value, a left child and a right child. (Binary)
	'''
	
	def __init__(self, value, left = None, right = None):
		self.left = left
		self.right = right
		self.value = value

	def __str__(self):
		return str(self.value)


	def depth(self, total = 0):
		'''
		Total depth of the tree until it's deepest leaf
		'''
		if self.left == None and self.right == None:
			return total
		return self.left.depth(total + 1) or self.right.depth(total + 1)

	def isNode(self):
		'''
		if a node has children i.e. left or right, the it's a node
		else it is a leaf
		'''
		return self.left or self.right

	def isLeaf(self):
		'''
		if a node has no left or a right
		'''


# we just created a tree, with 1 as the parent and 2 & 3 as it's children (left & right respectively)
node = Node(1, Node(2), Node(3))

# let's get the sum of all the nodes of the tree

def total(node):
	if node == None: return 0
	return total(node.left) + total(node.right) + node

def product(node):
	if node == None: return 1
	return product(node.left) * product(node.right) * node

#print total(node)
#print product(node)