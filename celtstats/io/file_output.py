import os

def writeFile(filePath, stream, fileName='documentIndex') :
    outputFile = filePath + '/index/' + fileName + '.idx'
    print('writing output to file: ' + outputFile)
    outHandler = open(outputFile, "w+")

    for s in stream :
        print(s)
        outHandler.write(s)
