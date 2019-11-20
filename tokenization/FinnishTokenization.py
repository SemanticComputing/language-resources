import nltk
import csv


class Tokenization():

    def __init__(self):
        self.tokenizatior = self.setup_tokenizator()

    def setup_tokenizator(self):
        tokenizer = nltk.data.load('tokenizers/punkt/finnish.pickle')
        with open('abbreviations.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                print("Add abbreviation", row[0])
                tokenizer._params.abbrev_types.add(row[0])
        for i in range(0,301):
            tokenizer._params.abbrev_types.add(str(i))
        return tokenizer

    # Tokenization from finnish text to sentences, returns list of sentences
    def sentence_tokenization(self, text):
        if text != None:
            return self.tokenizer.tokenize(text)

    def word_tokenization(self, sent):
        pattern = r'''(?x)          # set flag to allow verbose regexps
                (?:[A-Za-z]\.)+                     # abbreviations(both upper and lower case, like "e.g.", "U.S.A.")
                | (?:[0-9]+\.)+                     # order numbers
                | (?:ao|eaa|em|eo|huom|jaa|jKr|jms|jne|ks|ma|ml|mrd|nk|no|ns|oto|puh|so|tjsp|tm|tms|tmv|ts|va|vrt|vs|vt|yo|mm|esim|ym|yms|eKr|tjms)\.     # abbreviations(both upper and lower case, like "e.g.", "U.S.A.")
                | (?:[0-9]+\:[a-zåäö]+)             # inflected numbers, 1:lle, 16:sta
                | (?:[A-ZÅÄÖa-zåäö]+\:[a-zåäö]+)    # inflected abbreviations: USA:ssa, EU:lle
                | \w+(?:-\w+)*                      # words with optional internal hyphens 
                | [][.,;"'?():_`-]                  # these are separate tokens; includes ], [
            '''
        return nltk.regexp_tokenize(sent, pattern)
