import pylab

def loadExpenses(filename):
  '''
  Given the expenses file name
  load the expenses and return
  then as a tuple.
  '''
  try:
    inFile = open(filename)
    prashant = []
    vivek = []

    for line in inFile:
      line = line.replace(',', '')
      values = line.split()
      if len(values) == 2:
        try:
          prashant.append(float(values[0]))
          vivek.append(float(values[1]))
        except:
          continue

    inFile.close()
  except Exception, e:
    raise e

  return (prashant, vivek)


def plotExpenses(user):
  '''
  Given values of a user,
  plot the expenses on the y axis
  and the dasys on the x axis
  '''
  pylab.figure(1)
  pylab.title('Expenses over time')
  pylab.xlabel('Days')
  pylab.ylabel('Expenses')

  ps, = pylab.plot(range(len(user[0])), user[0], 'b-', label='Prashant')
  vs, = pylab.plot(range(len(user[1])), user[1], 'r-', label='Vivek')

  pylab.legend(handles=[ps, vs])
  pylab.show()

# extract expenses from the text file
expenses = loadExpenses('all_expenses.txt')
# plot graphs
plotExpenses(expenses)
