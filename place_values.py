def tens(nn):
    '''
    given two digit number `nn`, returns
    the text value for that nmber. `nn`
    can only range mentioned below
    '''
    num = str(nn)
    r = list(map(lambda v: str(v * 10), range(1, 11)))
    print(r)
    print(nn, ' --> ', nn in r)
    if nn not in r:
        return False
    return num[-2]


def units(n):
    '''
    given a single digit `n`, returns
    the text value for that digit. `n`
    can only range from 0 to 9
    '''
    num = int(n)
    if num not in range(11):
        return False
    units = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    return units[num]


def place_value(n):
    '''
    given a number, convert it into a textual form (indian)
    style and return the text. Eg: 12345, would return

    `twelve thousand three hundered and forty five`
    '''
    num = str(n)
    l = len(num)
    break_of = 2
    until = 3
    print(num[-3:])
    return [num[i:i + break_of] for i in list(range(0, l - until, break_of))]


print(place_value(1516361))
print(place_value(516361))
# print(place_value(500000000))
# print(place_value(1000))
