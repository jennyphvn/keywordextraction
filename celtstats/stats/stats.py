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

def freqWordsDoc(document, word):
    count = 0
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'google' in line:
            count += 1
    f.close()
    f = open('document_3456.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'amazon' in line:
            count += 1
    f.close()
    f = open('document_7788.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'paradise' in line:
            count += 1
    f.close()
    print(count)

#def rankWordsDoc(document, word):

def wordBeginLetterDoc(document, word):
    beginlist = {}
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for line in doc:
        for word in line:
            if 'a' in word:
                beginlist += [word]
    f.close()
    f = open('document_3456.txt','r')
    doc = f.readlines()
    for line in doc:
        for word in line:
            if 'a' in word:
                beginlist += [word]
    f.close()
    f = open('document_7788.txt','r')
    doc = f.readlines()
    for line in doc:
        for word in line:
            if 'a' in word:
                beginlist += [word]
    f.close()
    return beginlist

def wordEndLetterDoc(document, word):
    endList = {}
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for i in range(len(doc)):
         endList.append(doc[i].strip('\n'))
    f.close()
    f = open('document_3456.txt','r')
    doc = f.readlines()
    for i in range(len(doc)):
         endList.append(doc[i].strip('\n'))
    f.close()
    f = open('document_7788.txt','r')
    doc = f.readlines()
    for i in range(len(doc)):
         endList.append(doc[i].strip('\n'))
    f.close()
    return endList

def freqDocs(word): #given a word, return a list of the documents where that word appears
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'more' in line:
            print("document_1122")
    f.close()
    f = open('document_3456.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'more' in line:
            print("document_3456")
    f.close()
    f = open('document_7788.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'more' in line:
            print("document_7788")
    f.close()

def freqDocsWords(count, k): #given a count, return a list of documents that have that number of words, because the
                             #result can be long, return only k documents (where k is an integer)
    f = open('document_1122.txt','r')
    doc = f.readlines()
    if len(doc) == 56:
        print("document_1122")
    f.close()
    f = open('document_3456.txt','r')
    doc = f.readlines()
    if len(doc) == 56:
            print("document_3456")
    f.close()
    f = open('document_7788.txt','r')
    doc = f.readlines()
    if len(doc) == 56:
            print("document_7788")
    f.close()

def freqWordsSizeDoc(document, word): #given a document name, return the result of the number of times that word
                                      #appear in that document divided by the number of unique words in that document.
    endList = {}
    count = 0
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'google' in line:
            count += 1
    f.close()
    division = (count / len(doc))
    print(division)
    return endList

def augmentedCountWord(document, word): #given a document and a word, return the following computation: 0.5 +
                                        # (0.5 * number of times that word appears in the document/number of times of the most common word in that
                                        # document).
    endList = {}
    count = 0
    f = open('document_1122.txt','r')
    doc = f.readlines()
    for line in doc:
        if 'google' in line:
            count += 1
    f.close()
    aug = (0.5 + (0.5 * count))
    print(aug)
    return endList
