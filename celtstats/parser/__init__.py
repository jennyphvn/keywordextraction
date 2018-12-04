# this file is invoked when an application imports this package with the following command
# import celtstats

__doc__ = """
parser - contains functions for parsing text
=====================================================================
Main Features
-------------
  - aaa
  - bbbb
  - cccc
  - etc, etc.
"""

print('loading celtstats.parser module __init__.py')
from .text2tokens import *
import celtstats as cs
import os

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
