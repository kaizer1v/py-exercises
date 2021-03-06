'''
This is implementing a swap sort algorithm
to a given list
'''

def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final mod L: ", L)


l = [11, 9, 7, 6, 5, 0]
print(swapSort(l))
print(modSwapSort(l))
