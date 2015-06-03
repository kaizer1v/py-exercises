# import regular expression
import re

# A function to create a dictionary of words along with the number of occurances within a given file
def word_count(sourceFilename, targetFilename):
	# f = open(sourceFilename, 'r')
	with open(sourceFilename) as f:
		lines = f.readlines()

	dictionary = {}
	for line in lines:
		line = line.strip('\n')
		words = line.split(' ')
		for word in words:
			if word not in dictionary:
				# word = word.strip('@#%^&*`~()[]{}!\'\"?<>/-_;:,.\n').lower()
				word = re.sub('[^A-Za-z0-9]+', '', word.lower())
				dictionary[word] = 1
			else:
				dictionary[word] += 1

	f.close()
	fw = open(targetFilename, 'w')
	fw.write(str(dictionary))
	fw.close()

word_count('alice.txt', 'alice_dict.txt')