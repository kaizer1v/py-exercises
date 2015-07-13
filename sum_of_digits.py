def sumDigits(N):
  '''
  N: a non-negative integer
  '''
  # Your code here
  if type(N) == int and N >= 0:
    if N in range(0, 10):
      return N
    else:
      return sumDigits(N / 10) + (N % 10)