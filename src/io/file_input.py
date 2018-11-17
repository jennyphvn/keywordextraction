import os
fs = os.listdir('../../texts/input')

for file in fs:
    print('input file is: ' + file)
    docName = file[:file.find('.')]

    outputFile = '../../texts/output/' + docName + '.out'
    outHandler = open(outputFile, "w+")

    print('output file is: ' + outputFile)

    with open('../../texts/input/' + file) as f:
        for line in f:
            print(line)
            outHandler.write(line)
