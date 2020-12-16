'''
Given an n-by-n array `a` of n^2 distinct integers, design an algorithm that runs
in time proportional to `n log n` to find a local minimum:

an pair of indices i and j such that

* a[i][j] < a[i+1][j]
* a[i][j] < a[i][j+1]
* a[i][j] < a[i-1][j]
* a[i][j] < a[i][j-1]

(assuming the neighboring entry is in bounds).

Hint: Find the minimum entry in row n/2, say a[n/2][j].
If it's a local minimum, then return it. Otherwise, check it's two vertical
neighbors a[n/2-1][j] and a[n/2+1][j].
Recur in the half with the smaller neighbor.
'''
def local_minimum_matrix():
  pass
