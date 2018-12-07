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
def rankWordsDoc(document,word):
    d=cs.parser.documentIndex.items()
    listofwords=[]
    listofcounts=[]

    for k,v in d:
        c=v[0]
        d2=v[1]

        for key,value in d2.items():

            listofcounts += [value]
            listofwords += [key]

            return(sorted(listofwords, reverse=True)[:4], sorter(listofcounts, reverse=True)[:4])

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

def WordsSizeDoc(document, size):
    d=cs.parser.documentIndex[document][1]

    listofwords = []
    for key, value in d.items():
        if key == word :
            result = value

        return result

def freqdocscount(word):
    d=cs.parser.wordIndex.items()

    doc_list = []

    for key,value in d:
        if value[0] == count:
            for doc in value[1]:
                if doc not in docs_list:
                    docs_list +=[doc]

            return docs_list[:k]

def freqDocs(word): #given a word, return a list of the documents where that word appears

def freqDocsWords(count, k): #given a count, return a list of documents that have that number of words, because the
                             #result can be long, return only k documents (where k is an integer)


def freqWordsSizeDoc(document, word): #given a document name, return the result of the number of times that word
                                      #appear in that document divided by the number of unique words in that document.
    d_new = cs.parser.documentIndex[document][0]
    d = cs.parser.documentIndex[document][1]

    for key,value in d.items():
        if key == word:
            result = value / d_new

    return result

def augmentedCountWord(document, word): #given a document and a word, return the following computation: 0.5 +
                                        # (0.5 * number of times that word appears in the document/number of times of the most common word in that
                                        # document).
    d = cs.parser.documentIndex[document][1]

    for key,value in d.items():
        values.append(value)

    sorted_num = sorted(values)

    unique_nums = []
    for x in sorted_num:
        if x in sorted_num:
            if x not in unique_nums:
                unique_nums.append(x)

    result = 0.5 + (num / unique_nums[-1])

    return result
