import pylab

principle = 10000
interestRate = 0.05
years = 20
values = []

for i in range(years + 1):
    values.append(principle)
    principle += principle * interestRate


# pylab.figure(1)
pylab.plot(range(years + 1), values, 'ro')  # contains (x, y)

# Adding some titles and text
pylab.title('At 5% growth, compounded Anually.')
pylab.xlabel('Years')
pylab.ylabel('Value of Principal (INR)')

# Finally showing the graph
pylab.show()
