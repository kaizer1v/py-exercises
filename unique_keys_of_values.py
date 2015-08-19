def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, 
    empty list if none.
    '''
    # the Goal is to create a dictionary like so
    # { value: [times, key], ... }
    # where every value of the aDict stores a number of times it occurs
    #   along with the corresponding key
    
    
    # create a temporary dictionary
    temp = {}
    
    # loop through every element in aDict
    for key in aDict:
        
        if aDict[key] in temp:
            # print temp[aDict[key]][0], temp[aDict[key]]
            temp[aDict[key]][0] += 1
        else:
            temp[aDict[key]] = [1, key]
        
    # create an empty keysArr
    keysArr = []
    # for every elem in the temp dictionary
    for elem in temp:
        # check if the 'times' is exactly 1
        if temp[elem][0] == 1:
            # if so, append it to keysArr
            keysArr.append(temp[elem][1])
    
    # sort the keysArr and return it
    keysArr.sort()
    return keysArr





# Test Cases ---------
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print uniqueValues(aDict)
# should return [1, 3, 8]


aDict = {1: 1, 2: 1, 3: 1}
print uniqueValues(aDict)
# should return []

aDict = []
print uniqueValues(aDict)
# should return []