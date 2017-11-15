def count_match(s, match):
    '''
    Write a program that prints the number of
    times the string 'bob' occurs in s.
    For example, if s = 'azcbobobegghakl',
    then your program should print the number
    of times the string 'bob' appears in the string.
    '''
    count = 0
    while 'b' in s:
        bi = s.index('b')
        if s[bi:bi + 3] == match:
            count += 1
        s = s[bi + 1:]
    print count


count_match('bobaobboaodbaobobaobbob', 'bob')
count_match('booboboodobdobobodobdob', 'bob')
count_match('abdabadbababab', 'bab')
