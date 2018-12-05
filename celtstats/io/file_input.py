
import os
import celtstats.parser as pr
import celtstats.buildDiction as bd

def readFiles(filesPath) :
    fs = os.listdir(filesPath + '/input')

    for file in fs:
        #returns a list of things
        print('input file is: ' + file)
        docName = file[:file.find('.')-1]
                    #splicing a list
        outputFile = filesPath + '/output/' + docName + '.out'
        outHandler = open(outputFile, "w+")

        print('output file is: ' + outputFile)

        with open(filesPath + '/input/' + file) as f:
            #each line in file
            for line in f:
                print(type(line))
                cleanlist = []
                line2 = pr.useRegularExpression(line)
                for x in line2 :
                    if x not in pr.sw:
                        if x not in pr.punctuationMarksList:
                            cleanlist += [x]
                print(line)
                outHandler.write(line)

def readParsedFiles(filesPath) :
    fs = os.listdir(filesPath + '/output')

    for file in fs :
        print('input file is: ' + file)
        print('output file is: ' + filesPath + file)

        with open(filePath + file) as f :
            for line in f :
                line2 = pr.useRegularExpression(line)

def createDocumentIndexDictionary(path):
    fs = os.listdir(path)   # returns a list with the names of the files in a given directory

    for file in fs:         # let's iterate over the contents of that list
        print('input file is: ' + file)
        docName = file[:file.find('.')]

        with open(path + file, encoding='ISO-8859-1') as f:  # opens the file

            val_1 = 0      # initializes an empty counter
            val_2 = {}     # initializes an empty dictionary

            # if the file name is already in th the dictionary
            if file in cs.parser.documentIndex :
                val_1 = cs.parser.documentIndex[file][0]  # retrieves 1st element of the tuple: the counter
                val_2 = cs.parser.documentIndex[file][1]  # retrieves 2nd element of the tuple: a dictionary

            else :
                # if is a new entry in the dictionary, the tuple has to be
                # initialized with a counter of 1 and the empty dictionary
                cs.parser.documentIndex[file] = (1, {})

            # regardless if it's a new or existing document in the dictionary
            # populate the internal tuple!
            for line in f :                      # iterates over the lines in file f
                line2 = line.split()             # uses python string function split to create a list of words
                                                 # out of the each line in the file
                # now le'ts iterate over the words
                for word in line2 :
                    # if a word is found in the dictionary
                    if word in val_2 :
                        val_3 = val_2[word]      # retrieves the counter given the word as key
                        val_2[word] = val_3 + 1  # increments counter by one and sets in the dictionary

                    # if athe word is  not found in the dictionary
                    else :
                        val_2[word] = 1          # initialize the value of that dictionary with 1, using the word as key
                        val_1 += 1               # increments the outer counter because a new word in the document was found

                    cs.parser.documentIndex[file] = (val_1, val_2) # updates the entry in the external dictionary by creating
                                                                   # a tuple with the previously generated values
