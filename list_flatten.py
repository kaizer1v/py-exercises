l = [[2, 3, 5], [12], [[2, 4, 6], [23, 6]]]
print([item for sublist in l for item in sublist])


def has_list(lst):
    try:
        set(lst)
    except:
        return True
    return False

# [1, 2, [3, 4]]


def flatten_list(lst):
    flt_lst = []
    for item in lst:
        if type(item) == list:
            return flatten_list(item)
        else:
            flt_lst.append(item)
    return flt_lst

'''
Javascript logic

return arr.reduce(function(acc, x) {
    return acc.concat(x && x.constructor === Array ? arrayFlatten(x) : x)
}, [])
'''

# def
#     return reduce(flat, [1, 2, [4, 5]])


def flat(x, y):
    if type(y) == list:
        return flatten(y)
    return y
