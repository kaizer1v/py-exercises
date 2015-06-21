"""
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
"""

count = 0
while 'b' in s:
  bi = s.index('b')
  if s[bi:bi+3] == 'bob':
    count += 1
  s = s[bi+1:]
  #print bi, s, count
print count