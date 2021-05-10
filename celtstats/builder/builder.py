import celtstats as cs
import os

def builddict_1(dict = 'documentIndex'):
        fs = os.listdir('./texts/output')

        for file in fs :
            print('input file is: ' + file)
            docname = file[:file.find('.')]
            with open('./texts/output/' + file, encoding='ISO-8859-1') as f:
                    token_words = cs.parser.text2tokens(f)

                    count_unique_words = 0
                    for token in token_words:
                            if token in token_words:
                                count_unique_words += 1

                    token_counts = {}
                    for token in token_words:
                            count_each_word = token_words.count(token)
                            token_counts[token] = count_each_word

                    tuple = (count_unique_words, token_counts)
                    cs.parser.documentIndex[docname] = tuple

def builddic_2(stream, dict = 'wordIndex'):
    fs = os.listdir('./texts/output')

    for file in fs :
        print('input file is: ' + file)
        docname = file[:file.find('.')]

        with open('./texts/output/' + file, encoding='ISO-8859-1') as f:
            token_words = cs.parser.text2tokens(f)
            for token in token_words:
                if token in cs.parser.wordindex:
                    val_1 = cs.parser.wordindex[token][0]
                    val_2 = cs.parser.wordindex[token][1]
                    if docname not in val_2:
                        val_2 += [docname]
                        val_1 += 1
                    cs.parser.wordindex[token] = (val_1, val_2)
                else:
                    cs.parser.wordindex[token] = (1, [docname])
                
def builddic_3(stream, dict = 'indexAugmentedCount'):
    fs = os.listdir('./texts/output')

    for file in fs :
        print('input file is: ' + file)
        docname = file[:file.find('.')]

        with open('./texts/output/' + file, encoding='ISO-8859-1') as f:
            token_words = cs.parser.text2tokens(f)
            for token in token_words:
                if token in cs.parser.wordindex:
                    val_1 = cs.parser.wordindex[token][0]
                    val_2 = cs.parser.wordindex[token][1]
                    if docname not in val_2:
                        val_2 += [docname]
                        val_1 += 1
                    cs.parser.wordindex[token] = (val_1, val_2)
                else:
                    cs.parser.wordindex[token] = (1, [docname])
