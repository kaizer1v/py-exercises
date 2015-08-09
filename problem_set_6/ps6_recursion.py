# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if len(aStr) == 1: return aStr
    return reverseString(aStr[1:]) + aStr[0]


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO.

    #base case is

    # the .index will always return the 1st occurance's index
    try:
        word.index(x[0])
    except:
        if len(x) == 0:
            return True
        else:
            return False
        
    return x_ian(x[1:], word[word.index(x[0]) + 1:])
    


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.

    # base case is, whenever I have a text whose length is smaller than the lineLength, simply return it
    if len(text) <= lineLength: return text

    # otherwise, we need to take the part from 0-lineLength + \n + do the same thing for the remaining text
    return text[:lineLength] + '\n' + insertNewlines(text[lineLength:], lineLength)