import os
import celtstats.parser as pr

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
                print((type(line))
                line2 = pr.useRegularExpression(line)
                            #invoking function from parser
                print(line)
                outHandler.write(line2)
