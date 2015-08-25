import string
import pylab


def loadWords(filePath):
  '''
  Given a file path, load all the
  tempratures into an array and return.
  '''
  try:
    inFile = open(filePath, 'r', 0)
    high = []
    low = []
    # loop through every line
    for line in inFile:
      # split every line into fields
      fields = line.split()

      # filter out only the relevant data
      if len(fields) == 3 and fields[0].isdigit():
        high.append(int(fields[1]))
        low.append(int(fields[2]))
    
  except IOError:
    print 'File doesn\'t exist.'

  return (low, high)



def plotTempratures(low, high):
  '''
  Given a set of low and high
  tempratures, plot a graph that
  shows the difference in temprature 
  everyday.
  '''

  if len(low) == len(high):
    days = []
    tempDiff = []
    for i in range(len(low)):
      days.append(i)                       # x-axis
      tempDiff.append(high[i] - low[i])    # y-axis

    pylab.plot(days, tempDiff)
    pylab.title('Boston July Temperatures')
    pylab.xlabel('Number of Days from 1st July')
    pylab.ylabel('Temprature Difference')
    pylab.show()



# load the tempratures
tempratures = loadWords('tempratures.txt')
plotTempratures(tempratures[0], tempratures[1])