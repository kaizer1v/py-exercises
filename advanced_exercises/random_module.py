'''
There are 4 kinds of simulation models
1. Deterministic vs Stochastic
2. Static vs Dynamic
3. Discrete vs Continuous

-> Deterministic simulation are defined by the model, re-running the
  simulation will not change the outcome.
-> Stochastic simulation include randomness which means, different
  runs with same initial conditions can generate different results.
-> Discrete models values of the variable are enumerable
-> Continuous on the other hand are not enumerable 
'''
import random

# Print a random number between 5 and 10
## print random.randint(5, 10)

# print random choice from the array of fruits
## print random.choice(['apple', 'banana', 'orange'])

def genEven():
  '''
  Returns a random even number x, where 0 <= x < 100
  '''
  return random.choice([x for x in range(0, 100) if x % 2 == 0])
  # could also be written as
  # return random.randrange(0, 100, 2)
  

def deterministicNumber():
  '''
  Deterministically generates and returns an even number between 9 and 21
  '''
  # Your code here
  random.seed(0)
  return random.randrange(10, 21, 2)
  

def stochasticNumber():
  '''
  Stochastically generates and returns a uniformly distributed even number between 9 and 21
  '''
  # Your code here
  random.randrange(10, 21, 2)
  
  
def distributionSimulation():
  '''
  This function determines
  to see what a distribution
  looks like.
  '''
  
  ## Case 1: checking distribution simulation of .randrange method
  d1 = {}
  for i in range(10000):
    x = random.randrange(10)
    d1[x] = d1.get(x, 0) + 1
    
    
  ## Case 2: checking distribution simulation of .randint method
  d2 = {}
  for i in range(10000):
    x = random.randint(0, 10)
    d2[x] = d2.get(x, 0) + 1
    
  
  ## Case 3: checking distribution simulation of .random() * 10 method
  d3 = {}
  for i in range(10000):
    x = int(random.random() * 10)
    d3[x] = d3.get(x, 0) + 1
    
  print d1
  print d2
  print d3
  
distributionSimulation()


## Example 1: Deterministic Randomness
mylist = []

for i in xrange(random.randint(1, 10)):
  random.seed(0)
  if random.randint(1, 10) > 3:
    number = random.randint(1, 10)
    if number not in mylist:
      mylist.append(number)
print mylist


## Example 2: Also a Deterministic Randomness
mylist = []

random.seed(0)
for i in xrange(random.randint(1, 10)):
  if random.randint(1, 10) > 3:
    number = random.randint(1, 10)
    mylist.append(number)
  print mylist



def coinFlip(numFlips):
  '''
  Determines the number of times
  the coin was flipped and resulted
  in heads or tails. Dependent on 
  random.

  @param <int> - numFlips = number of times
    you want to flip the coin

  @return <float> - ratio of total heads that resulted
    out of the total flips. 
  '''
  heads = 0.0
  for i in range(numFlips):
    if random.random() < 0.5:
      heads += 1
    
  return heads / numFlips