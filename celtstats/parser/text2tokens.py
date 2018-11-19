"""text2tokens functions

This module does abc

Todo:
    * Clean code
    * Add return values

"""

import re
import string

# stop words to be removed
sw = ['i', 'a', 'am', 'about', 'an', 'are', 'as', 'at', \
      'be', 'by', 'com', 'for', 'from', 'he', 'how', 'in', \
      'is', 'it', 'of', 'on', 'or', 'she', 'that', 'the', \
      'they', 'this', 'to', 'was', 'what', 'when', 'where', \
      'who', 'will', 'with', 'the', 'www', 'you', 'we']

#
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
    newStrem = stream
    if option== 'alphanum' :
        newStream = re.sub(r'[^a-zA-Z0-9 ]',r'',stream)
    elif option == 'alpha' :
        newStream = re.sub(r'[^a-zA-Z ]',r'',stream)
    elif option == 'num' :
        newStream = re.sub(r'[^0-9 ]',r'',stream)
    elif option == 'symb' :
        newStream = re.sub(r'[a-zA-Z0-9]',r'',stream)

    return newStream
