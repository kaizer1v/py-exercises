def first(first, *args):
    '''testing out dynamic argument passing usig *args'''
    # print first
    for a in args:
        print("the argument - {}, you passed is of {}".format(a, type(a)))

first(123, 'asdf', False, 1.55, [1, 2, 4], {'a': 23}, (33, 55, 77))


def second(first, **kwargs):
    '''testing out kwargs i.e. keyword arguments'''
    # print first
    for key, value in kwargs.iteritems():
        print("{} ==> {}".format(key, value))

second('second', str="vivek", float=12.34, bool=True, ll=[1, 5, 3])
