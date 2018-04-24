#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.


def remove_adjacent(nums):
    # return
    y = [0]
    for n in x:
        if n != y[len(y) - 1]:
            y.append(n)
    y.remove(0)


# Write a function remove_duplicates that takes in a list and removes
# elements of the list that are the same.
def remove_duplicates(lst):
    new_lst = []
    for key, l in enumerate(lst):
        if l not in lst[key + 1:]:
            new_lst.append(l)
    return new_lst


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    new_list = list1 + list2
    new_list = new_list.sort()
    return new_list

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.

# F. Given a list of items, return the index of the last
# occurance of an item in the list. If it is unable
# to find the item, should return "item not found"


def last_instance(lst, item, i=0):
    try:
        index = lst.index(item, i)
        return last_instance(lst, item, index + 1)
    except:
        if i - 1 < 0:
            return "item does not exist"
        return i - 1

# G. Given a list, for eg: ['apples', 'bananas', 'lemons']
# return a string like 'apples, bananas and lemons', by adding
# adding 'and' before the last item.


def and_item(lst):
    if len(lst) > 2:
        return ', '.join(lst[:-1]) + ' and ' + lst[-1]
    return ' and '.join(lst)


# Simple provided test() function used in main() to #print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    #print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
    #print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    #print
    #print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])

    #print
    #print 'last_instance'
    test(last_instance(['a', 'c', 'u', 'z', 'c', 'c', 'zz'], 'c'))
    test(last_instance(['a', 'c', 'u', 'z', 'c', 'c', 'zz'], 'a'))
    test(last_instance(['a', 'c', 'u', 'z', 'c', 'c', 'zz'], 'zz'))
    test(last_instance(['a', 'c', 'u', 'z', 'c', 'c', 'zz'], 'dd'))

    #print
    #print 'and_item'
    test(and_item([]))
    test(and_item(['one']))
    test(add_item(['one', 'two']))
    test(add_item(['one', 'two', 'three', 'four']))


if __name__ == '__main__':
    main()
