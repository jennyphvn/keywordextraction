import os
import celtstats.parser as pr
#import celtstats.buildDiction as bd

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
