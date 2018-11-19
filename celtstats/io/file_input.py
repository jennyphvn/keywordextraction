import os

def readFiles(filesPath) :
    fs = os.listdir(filesPath + '/input')

    for file in fs:
        print('input file is: ' + file)
        docName = file[:file.find('.')]

        outputFile = filesPath + '/output/' + docName + '.out'
        outHandler = open(outputFile, "w+")

        print('output file is: ' + outputFile)

        with open(filesPath + '/input/' + file) as f:
            for line in f:
                print(line)
                outHandler.write(line)
