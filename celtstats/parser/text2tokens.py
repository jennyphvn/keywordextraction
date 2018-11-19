"""text2tokens functions

This module does abc

Todo:
    * Clean code
    * Add return values

"""

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


def removeNumbers(line) :
    for w in line.split() :
        print(w)
