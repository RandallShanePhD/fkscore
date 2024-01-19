# Flesch-Kinkaid Readability Scoring

import re
import string


class fkscore:
    """ Flesch Kincaid Readability Score
    text = "The quick red fox jumped over the lazy brown dog."
    stats:
     sentences = 1
     words = 10
     syllables = 12
    score
     readability = 86.705
     read_grade = 6th Grade
     calc_grade =
    """

    def __init__(self, text):
        """
        Input: UTF-8 text as str

        Output (stats):
            stats['num_words']
            stats['num_syllables']
            stats['num_sentences']
        Output (score):
            score['readability']  # Calculated F-K Readability
            score['read_grade']   # Permuted F-K Grade Reading Level
        """
        self.stats = {}
        self.basic_stats(text)
        self.score = {}
        self.fk_score()
        self.permute_grade()
        self.calc_grade()

    def basic_stats(self, rawtext):
        # Primary text segregation function
        output = {'sentences': 0, 'words': 0, 'wordblock': [], 'errors': []}

        # Split on \n or . ! ? for sentences
        wip_text = re.split('''(\n|(\.+|!+|\?+) +)''', rawtext)

        # Split Sentences (keep punctuation)
        for i, s in enumerate(wip_text):
            try:
                if s is not None and len(s.strip()) > 1 and i < len(wip_text):
                    try:
                        punctuation = wip_text[i + 1]
                    except Exception:
                        punctuation = ''
                    sentence_text = (wip_text[i] + punctuation).replace('\n', '')
                    output['sentences'] += 1

                    translator = str.maketrans('', '', string.punctuation)
                    words = sentence_text.translate(translator).split(' ')
                    output['words'] += len(words)
                    wordblock = output['wordblock'] + words
                    output['wordblock'] = [x for x in wordblock if x != '' and x is not None]
            except Exception as exc:
                output['error'].append(exc)

        self.stats['num_sentences'] = output['sentences']
        self.stats['num_words'] = output['words']

        # Syllable computation
        def num_syllables(word):
            word = word.lower()
            count = 0
            vowels = "aeiouy"
            if word[0] in vowels:
                count += 1
            for index in range(1, len(word)):
                if word[index] in vowels and word[index - 1] not in vowels:
                    count += 1
            if word.endswith("e"):
                count -= 1
            if count == 0:
                count += 1
            return count

        self.stats['num_syllables'] = sum([num_syllables(x) for x in output['wordblock']])

    def fk_score(self):
        # Flesch Reading Ease Score (FRE)
        self.score['readability'] = round(206.835 -
                                          (1.015 * (self.stats['num_words'] / self.stats['num_sentences'])) -
                                          (84.6 * (self.stats['num_syllables'] / self.stats['num_words'])), 3)

    def permute_grade(self):
        # FRE read_grade level
        self.score['read_grade'] = '4th Grade or Below'
        if round(self.score['readability'], 0) >= 90:
            self.score['read_grade'] = '5th Grade'
        elif round(self.score['readability'], 0) >= 80:
            self.score['read_grade'] = '6th Grade'
        elif round(self.score['readability'], 0) >= 70:
            self.score['read_grade'] = '7th Grade'
        elif round(self.score['readability'], 0) >= 60:
            self.score['read_grade'] = '9th Grade'
        elif round(self.score['readability'], 0) >= 50:
            self.score['read_grade'] = '11th Grade'
        elif round(self.score['readability'], 0) >= 30:
            self.score['read_grade'] = 'College Level'
        else:
            self.score['read_grade'] = 'College Graduate'

    def calc_grade(self):
        # Calculated grade level
        self.score['calc_grade'] = round((0.39 * (self.stats['num_words'] / self.stats['num_sentences'])) +
                                         (11.8 * (self.stats['num_syllables'] / self.stats['num_words']))
                                         - 15.59, 3)


# Validation of results
# if __name__ == "__main__":
#     text = "The cat sat on the mat."
#     # text = "The quick red fox jumped over the lazy brown dog."
#     # text = "This sentence, taken as a reading passage unto itself, is being used to prove a point."
#     # text = "The Australian platypus is seemingly a hybrid of a mammal and reptilian creature."
#     f = fkscore(text)
#     print(f.stats)
#     print(f.score)
