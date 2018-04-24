def alternating_chars(s):
    '''
    Given a string like AABABBAB, you need to return how many chars need to be
    deleted so that no subsequent letters are the same
    Basically, AABABABBA should become ABABABA (return total chars to be
    deleted)
    '''

    toDel = 0
    for x in range(1, len(s)):
        if s[x] == s[x - 1]:
            toDel = toDel + 1
    # total = total - 1

    for index, char in enumerate(s):
        if s[index] == s[index - 1]


alternating_chars('AABABABBA')
