
import celtsats as cs
import os

def addToDoc(doc_name, count):
    cs.parser.documentIndex[doc_name]= ()
    t= (count,{})
    cs.parser.documentIndex[doc_name]= t

def addToInsideDoc(doc_name, stream):
    for word in stream:
        count= cs.parser.documentIndex[doc_name][0]
        d2= cs.parser.documentIndex[doc_name][1]
        count +=1
        if word in d2:
            count2= d2[word]
            d2[word]= count2 + 1
        else:
            d2[word]= 1
        tuple=(count, d2)
        cs.parser/documentIndex[doc_name]= tuple

    def readFiles(filesPath):
        fs= os.listdir(filesPath)
            for file in fs:
            print('input file is:' + file)
            addToDoc(file, 0)

            with open(filesPath + file, encoding='ISO-8859-1') as f:
                for line in f:
                    line2= line.split()
                    addtoInsideDoc(file, line2)


#for
#def buildDiction(document, words):
#    for w in words :''
#        documentIndex[document] = words
#one is going to be the key. one os going to be the value
