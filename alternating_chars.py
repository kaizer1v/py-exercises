# Given a string like AABABBAB, you need to return how many chars need to be
# deleted so that no subsequent letters are the same
# Basically, AABABABBA should become ABABABA (return total chars to be deleted)

total = int(input())
while(total):
    str = input()
    toDel = 0
    for x in range(1, len(str)):
        if str[x] == str[x - 1]:
            toDel = toDel + 1
    print(toDel)
    total = total - 1
