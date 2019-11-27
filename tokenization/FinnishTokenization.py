import nltk
import csv


class Tokenization():

    def __init__(self):
        self.tokenizatior = self.setup_tokenizator()

    # Setting up tokenizer for sentence tokenization
    # TODO: see, if this can be also replaced with a regex tokenization, as this does not take into account special cases similar to word tokenization
    def setup_tokenizator(self):
        tokenizer = nltk.data.load('tokenizers/punkt/finnish.pickle')
        with open('abbreviations.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                tokenizer._params.abbrev_types.add(row[0])
        for i in range(0,301):
            tokenizer._params.abbrev_types.add(str(i))
        return tokenizer

    # Tokenization from finnish text to sentences, returns list of sentences
    def sentence_tokenization(self, text):
        if text != None:
            return self.tokenizer.tokenize(text)

    # tokenizing text to a list of tokens (words, punctuation, etc.)
    def word_tokenization(self, sent):
        oldpattern = r'''
                (?x)                                                            # set flag to allow verbose regexps
                (?:[A-ZÖÄÅa-zöäå]\.)+(?=\s)                                     # abbreviations(both upper and lower case, like "e.g.", "U.S.A.")
                | (?:[0-9]+)(?=[.!?]\s+[A-ZÖÄÅ])                                # order numbers at end of a sentence
                | (?:[0-9]+\.)+(?=\s)                                           # order numbers
                | (?:ao|eaa|em|eo|huom|jaa|jKr|jms|jne|ks|ma|ml|mrd|nk|no|ns|oto|puh|so|tjsp|tm|tms|tmv|ts|va|vrt|vs|vt|yo|mm|esim|ym|yms|eKr|tjms)\.  # abbreviations
                | [/({\['"”».](?=\S)                                            # opening bracket/quotes
                | (?:\S+)(?=[.,;:?!(){}\[\]'"»”–-][.,;:?!(){}\[\]'"»”–-][.]*)   # case three punctuation marks: '... quoted!'.
                # | (?:\S+)(?=[.,;:?!(){}\[\]'"»”–-][.,;:?!(){}\[\]'"»”–-])     # case two punctuation marks: ... (something).
                | \S+(?=[.,;:?!(){}\[\]'"»”–-]+(?:\s|[.]|$))                    # word with punctuation at end
                | \w+(?=/\w+)
                | \S+
        '''
        added = self.compile_pattern()
        print("New pattern:", added)

        pattern = r'''(?x)          # set flag to allow verbose regexps
                (?:[A-ZÖÄÅa-zöäå]\.)+(?=\s)         # abbreviations(both upper and lower case, like "e.g.", "U.S.A.")
                | (?:[0-9]+)(?=[.!?]\s+[A-ZÖÄÅ])         # order numbers at end of a sentence
                | (?:[0-9]+\.)+(?=[ )])         # order numbers "14. ", "(47.)"
                | $abbr  # abbreviations
                | [/({\['"”».](?=\S)  # opening bracket/quotes
                | (?:\S+)(?=[.,;:?!(){}\[\]'"»”–-][.,;:?!(){}\[\]'"»”–-][.]) # case three punctuation marks: '... quoted!'.
                | (?:\S+)(?=[.,;:?!(){}\[\]'"»”–-][.,;:?!(){}\[\]'"»”–-]) # case two punctuation marks: ... (something).
                | \S+(?=[.,;:?!(){}\[\]'"»”–-]+(?:\s|[.]|$)) # word with punctuation at end
                | \w+(?=/\w+) # case: naimisissa/naimaton/leski ...
                | \S+
            '''
        pattern = pattern.replace('$abbr', added)
        print("Used pattern:",pattern)
        return nltk.regexp_tokenize(sent, pattern)

    def compile_pattern(self):
        pattern = '(?:$abbr)\.'
        with open('abbreviations.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            #for row in csv_reader:
            pattern = pattern.replace('$abbr',"|".join(['{0}'.format(x[0]) for x in csv_reader]))
        if '$abbr' in pattern:
            pattern = '(?:ao|eaa|em|eo|huom|jaa|jKr|jms|jne|ks|ma|ml|mrd|nk|no|ns|oto|puh|so|tjsp|tm|tms|tmv|ts|va|vrt|vs|vt|yo|mm|esim|ym|yms|eKr|tjms)\.'
        return pattern