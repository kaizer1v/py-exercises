import pandas as pd

## Think of vectors as Columns
counts = pd.Series([632, 1638, 569, 115])

## You can view the indexes or values directly from a Series
# print(counts.values)
# print(counts.index)

## You can even change the indexes to your custom ones like so
##   you can pass in an array of indexes which is the same size as the values and index will map it to resp value.
bacteria = pd.Series([632, 1638, 569, 115], index = ['Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes'])

print(bacteria['Firmicutes'])