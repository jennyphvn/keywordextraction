"""text2tokens functions

This module lists stop words to be removed, returns a list of the lines of text in text file, returns list of words in the text file

Todo:
    * Clean code
    * Add return values

"""

import re
import string

documentIndex = {}
wordIndex = {}
indexAgmentedCount = {}

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
        tokens += [line]
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
