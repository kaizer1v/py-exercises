class Stack(object):
	'''
	A stack is a data structure, which follows the LIFO approach
	LIFO: Last In First Out
	'''
	
	def __init__(self):
		self.items = []

	def __str__(self):
		print '[',
		for elem in self.items:
			print elem,',',
		print ']'

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return (len(self.items) == 0)