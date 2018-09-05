def mean(l):
    '''also called average'''
    return sum(l) / len(l)


def mode(l):
    '''max repeating value'''
    return max(set(l), key=l.count)


def median(l):
    '''get middle value'''
    l.sort()
    if len(l) % 2 != 0:
        return l[len(l) // 2]
    return mean([l[len(l) // 2], l[len(l) // 2 - 1]])


def skewed_towards(l):
    '''towards which side is the graph skewed'''
    if mean(l) > median(l):
        return 'right'
    elif mean(l) < median(l):
        return 'left'
    return 'center'
