import random

def rollDie():
	return random.choice([1, 2, 3, 4, 5, 6])

def rollN(n):
	'''
	given 'n' times to roll a die
	print the sequence of results
	n times
	'''
	result = ''
	for i in range(n):
		result += str(rollDie())
	return result

def getTarget(goal):
	'''
	For a given goal, i.e. a possible
	outcome, return the number of trials
	it took to reach that goal.
	'''
	numTrials = 0
	numRolls = len(goal)
	while True:
		numTrials += 1
		result = rollN(numRolls)
		if result == goal:
			return numTrials

# Check how many trials it takes to get 123456 in a row?
# print getTarget('123456')

def runSim(goal, numTrials):
	'''
	Given a goal and a limited set of trials,
	what is the probablity that you will reach
	that goal?
	'''
	total = 0
	for i in range(numTrials):
		total += getTarget(goal)
	avgTrials = total / float(numTrials)

	return (1 / avgTrials)

print 'Probability = ',
print runSim('11111', 100)