# Flesch-Kinkaid Readability Scoring

import pyphen
import re


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
        self.stats = {}
        self.basic_stats(text)
        self.score = {}
        self.fk_score()

    def basic_stats(self, text):
        words = [x for x in text.replace('-', ' ').split(' ') if x != '']
        self.stats['num_words'] = len(words)

        self.stats['num_sentences'] = len([x for x in re.split("(\. +|\? +|\! +)", text) if len(x) > 3])

        dic = pyphen.Pyphen(lang='en')
        self.stats['num_syllables'] = sum([len(dic.inserted(x).split('-')) for x in words])

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
