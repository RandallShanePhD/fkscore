# Flesch-Kinkaid Readability Scoring

import pyphen
import re
import string
import sys


class fkscore():

    def __init__(self, text):
        '''
        Input: UTF-8 text as str

        Output (stats):
            stats['num_words']
            stats['num_syllables']
            stats['num_sentences']
        Output (score):
            score['readability']  # Calculated F-K Readability Score
            score['grade']        # Permuted F-K Grade Reading Level
        '''
        self.splits = self.text_split(text)
        self.stats = {}
        self.basic_stats(text)
        self.score = {}
        self.fk_score()

    def basic_stats(self, rawtext):
        # Primary text segregation function
        output = {}
        output['sentences'] = 0
        output['words'] = 0
        output['wordblock'] = []
        output['errors'] = 0

        # Split on \n or . ! ? for sentences
        wip_text = re.split('''(\n|(\.+|\!+|\?+) +)''', rawtext)

        # Split Sentences (keep punctuation)
        for i, s in enumerate(wip_text):
            try:
                if s is not None and len(s.strip()) > 1 and i < len(wip_text):
                    try:
                        punctuation = wip_text[i + 1]
                    except:
                        punctuation = ''
                    sentence_text = (wip_text[i] + punctuation).replace('\n', '')
                    output['sentences'] += 1

                    # Split Text within sentences (list of lists, no punctuation)
                    translator = str.maketrans('', '', string.punctuation)
                    words = sentence_text.translate(translator).split(' ')
                    # print('APPEND WORDS: ', words)
                    output['words'] += len(words)
                    wordblock = output['wordblock'] + words
                    output['wordblock'] = [x for x in wordblock if x != '' and x is not None]
            except:
                output['error'] += 1

        self.stats['num_sentences'] = output['sentences']
        self.stats['num_words'] = output['words']

        # Syllables with pyphen
        dic = pyphen.Pyphen(lang='en')
        self.stats['num_syllables'] = sum([len(dic.inserted(x)) for x in wordblock])

    def fk_score(self):
        # Flesch-Kincaid readability score
        self.score['readability'] = round(206.835 -
                                          (1.015 * (self.stats['num_words'] / self.stats['num_sentences'])) -
                                          (84.6 * (self.stats['num_syllables'] / self.stats['num_words'])), 3)

        # Flesch-Kincaid grade level
        self.score['grade'] = '4th Grade or Below'
        if self.score['readability'] >= 90:
            self.score['grade'] = '5th Grade'
        elif self.score['readability'] >= 80:
            self.score['grade'] = '6th Grade'
        elif self.score['readability'] >= 70:
            self.score['grade'] = '7th Grade'
        elif self.score['readability'] >= 60:
            self.score['grade'] = '9th Grade'
        elif self.score['readability'] >= 50:
            self.score['grade'] = '11th Grade'
        elif self.score['readability'] >= 30:
            self.score['grade'] = 'College Level'
        else:
            self.score['grade'] = 'College Graduate'
