def builddict_1(stream, dict = 'documentIndex'):
        fs = os.listdir('./texts/output')

        for file in fs :
            print('input file is: ' + file)
            docname = file[:file.find('.')]
            with open('./texts/output/' + file) as f:
                    token_word = cs.parser.text2tokens(f)

                    count_unique_words = 0
                    for token in token_words:
                            if token in token_words:
                                count_unique_words += 1

                    token_counts = {}
                    for token in token_words:
                            count_each_word = token_words.count(token)
                            token_counts[token] = count_each_word

                        tuple = (count_unique_words, token_counts)
                        cs.parser.documentindex[docnam] = tuple
