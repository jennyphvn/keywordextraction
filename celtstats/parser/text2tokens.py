"""text2tokens functions

This module lists stop words to be removed, returns a list of the lines of text in text file, returns list of words in the text file
removes numerals and special characters from input text and returns text with those characters removed

"""
# https://www.sanfoundry.com/python-program-count-occurrences-word-text-file/
# to use these anywhere else in the code:
# import celtstats as cs
# then use cs.parser to invoke parser in this folder

import re
import string

documentIndex = {}
wordIndex = {}
indexAugmentedCount = {}

sw =['i', 'a', 'am', 'about', 'an', 'are', 'as', 'at', \
      'be', 'by', 'com', 'for', 'from', 'he', 'how', 'in', \
      'is', 'it', 'of', 'on', 'or', 'she', 'that', 'the', \
      'they', 'this', 'to', 'was', 'what', 'when', 'where', \
      'who', 'will', 'with', 'the', 'www', 'you', 'we']

punctuationMarksList = ['!','@','#','$','%','^','&','*','(', \
                        ')','_','-','=','+',"'",'"', \
                        '1','2','3','4','5','6','7','8','9','0']

def text2tokens(stream) :

    """text2tokens function

    Args:
        * stream (list): list of lines of text

    Return:
        * list : of words

    """

    tokens = []
    for line in stream :
        line2 = line.split()
        for word in line2 :
           tokens += [word]
        print(line)

    return tokens

# example of using regular expressions, adapted from
# https://stackoverflow.com/questions/3939361/remve-specific-characters-from-a-string-in-python
# https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
def useRegularExpression(stream, option='alphanum') :
    newStream = stream
    if option== 'alphanum' :
        newStream = re.sub(r'[^a-zA-Z0-9 ]',r'',stream)
    elif option == 'alpha' :
        newStream = re.sub(r'[^a-zA-Z ]',r'',stream)
    elif option == 'num' :
        newStream = re.sub(r'[^0-9 ]',r'',stream)
    elif option == 'symb' :
        newStream = re.sub(r'[a-zA-Z0-9]',r'',stream)
    elif option == 'lower' :
        newStream = stream.lower()

    return newStream

def addToDoc(doc_name, count):
    cs.parser.documentIndex[doc_name] = ()
    t= (count, {})
    cs.parser.documentIndex[doc_name]= t

def addToInsideDoc(doc_name, stream):
    for word in stream:
        count= cs.parser.documentIndex[doc_name][0]
        d2= cs.parser.documentIndex[doc_name][1]
        count += 1
        if word in d2:
            count2= d2[word]
            d2[word]= count2 + 1
        else:
            d2[word] = 1
        tuple=(count, d2)
        cs.parser.documentIndex[doc_name]= tuple

def readFiles(filesPath):
    fs= os.listdir(filesPath)

    for file in fs:
        print('input file is:' + file)
        addToDoc(file, 0)

        with open(filesPath + file, encoding='ISO-8859-1') as f:
            for line in f:
                line2= line.split()
                addToInsideDoc(file, line2)
