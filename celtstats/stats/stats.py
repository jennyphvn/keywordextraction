"""stats functions

This module does abc

Todo:
    * Clean code
    * Add return values

"""

def avgValue(values) :
    """avgValue

    This function does
    """
    total = 0
    for v in values :
        total += v

    return total

def maxValue(values) :
    """maxValue

    This function does
    """
    max = 0
    for v in values :
        if v > max :
            max = v

    return max

def freWordsDoc(document, word):
    count = 0
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'google' in line:
            count += 1
    #do this with every document. choose different word
    print(count)
    f.close()

#def rankWordsDoc(document, word):

def wordBeginLetterDoc(document, word):
    beginlist = {}
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for line in doc:
        for word in line:
            if 'a' in word:
                beginlist += [word]
    return beginlist

def 
