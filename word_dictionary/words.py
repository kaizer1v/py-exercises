"""
This is a basic dicitonary genertor that generates a dictionary of words and their occurances
from a given source file (text file).
"""
import re


class dictionary(object):
    fileDictionary = {}

    def __init__(self, sourceFilename):
        # pass
        self.sourceFilename = sourceFilename
        self.fileDictionary = self.getDictionary()

    # returns all the lines as a list from the file.
    def getLines(self):
        with open(self.sourceFilename) as f:
            lines = f.readlines()
        toReturn = []
        for line in lines:
            toReturn.append(line.strip('\n'))
        return toReturn

    # gets a list of all the words, occuring multiple times from the file.
    def getAllWords(self):
        lines = self.getLines()
        words = []
        for line in lines:
            l = line.split(' ')
            for word in l:
                if word != '':
                    word = self.filterWord(word)
                    words.append(word)
        return words

    # a helper function to strip off special characters from all the words.
    def filterWord(self, word):
        return re.sub('[^A-Za-z0-9]+', '', word.lower())

    # a helper file to close the open file.
    def closeFile(self):
        self.sourceFilename.close()
        return True

    # this is the method that generates the dictionary from the file and
    #   adds it to the member variable fileDictionary and returns it.
    def getDictionary(self):
        lines = self.getLines()
        for line in lines:
            line = line.strip('\n')
            words = line.split(' ')
            for word in words:
                if word not in self.fileDictionary:
                    word = self.filterWord(word)
                    self.fileDictionary[word] = 1
                else:
                    self.fileDictionary[word] += 1
        return self.fileDictionary

    # a print method to print the complete dictionary.
    def printDictionary(self):
        sortedDict = sorted(self.fileDictionary.keys())
        for word in sortedDict:
            print('{:s} {:d}'.format(word, self.fileDictionary[word]))

    # a method that returns the number of occurances of a given word.
    def getWordOccurance(self, word):
        if word in self.fileDictionary:
            wordCount = self.fileDictionary[word]
        else:
            wordCount = 'Sorry, that word doesn\'t exist in this text.'
        return wordCount

    # a method to get the most occuring word other from the dictionary.
    def getMostOccuringWord(self):
        occurances = self.fileDictionary.values()
        occurances.sort()
        mostOccuring = occurances[len(occurances) - 2]
        for word, occ in self.fileDictionary.items():
            if occ == mostOccuring and word != '':
                return 'The word "%s" occurs %d times in the file.' % (word, occ)


# ============================
# EXECUTION:
alice_dict = dictionary('alice.txt')
alice_dict.printDictionary()
