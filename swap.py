def swapSort(L): 
    """ L is a list on integers """
    #print "Original L: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                #print L
    #print "Final L: ", L


def modSwapSort(L): 
    """ L is a list on integers """
    #print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                #print L
    #print "Final mod L: ", L


l = [11, 9, 7, 6, 5, 0]
#l = [11, 9, 7, 6, 5, 0]

x = 4

#print swapSort(l)
#print modSwapSort(l)
