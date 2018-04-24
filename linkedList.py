class Node(object):
	'''
	This class helps simulate the linked list
	datastructure. A node is a single entitiy within
	the linked list datastructure.
	'''

	def __init__(self, cargo = None, next = None):
		'''
		The cargo, refers to the value of a node.
		next, is a node to which this node will refer to.
		'''
		self.cargo = cargo
		self.next = next

	def __str__(self):
		return str(self.cargo)



def #printList(node):
	'''
	Note: this is actually outside the class.
	will #print all the nodes in a list
	'''
	while node:
		#print node 		# this will call the __str__ method automatically
		node = node.next
	#print

def #printListBackwards(node):
	'''
	Given a linked list, this fn #prints the link
	backwards. Note this is recursive function
	'''
	if node == None: return
	#printListBackwards(node.next)
	#print node,


# Lets create some nodes for a linked list
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# We also need to link each element to the other
n1.next = n2
n2.next = n3
n3.next = n4
# since n4 is not linked to any other, it is the 
# end of the linked list

#printList(n1)
#printListBackwards(n4)