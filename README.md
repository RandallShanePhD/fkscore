fkscore
====

Flesch Kincaid readability score for text

A Python module implementation of the Flesch Kincaid readability score algorithm.

The source code is released under the MIT License.

### Installation ###
    pip3 install fkscore

### Usage ###
For text in python represented as a string.

Takes text as string datatype.  Words can be on same or different lines.  Current version is English language only.  Email for support.

    import fkscore
    text = '...blah blah blah...'
    f = fkscore.fkscore(text)
    print(f.stats)
    print(f.score)

    OR

    from fkscore import fkscore
    text = '...blah blah blah...'
    f = fkscore(text)
    print(f.stats)
    print(f.score)

### Output ###
Output includes 2 dictionaries of information as follows:
* stats:
  * stats['num_words']
  * stats['num_syllables']
  * stats['num_sentences']
* score:
  * score['readability']  # Calculated F-K Readability Score
  * score['read_grade']   # Permuted F-K Grade Reading Level
  * score['calc_grade']   # Calculated K-K Grade Level

### Releases ###
Releases and additions will push to PyPi as needed. If there is a feature in master not built/pushed, and you want it to be, just ping me. 
Note that the validation and many examples for this algorithm implement lines of text for analysis. It is not required to use single lines. 
One classic example of this is the text of Moby Dick, which is evaluated to posess a readability score of 58.
This module is pure python and works with all python versions >= 3.5. It likely works with older versions but has yet been tested.


### History ###
This is maintained as an implementation of the Flesch-Kincaid algorithm which initially developed in 1948 by Rudolph Flesch. 
It was later revised by J. Peter Kincaid and his team for the U.S. Navy in 1975. The F–K formula was first used by the Army for 
assessing the difficulty of technical manuals in 1978 and soon after became a United States Military Standard. The goal of the 
algorithm is to provide an empirical basis for assessing the difficuly of understanding text.

### Algorithm ###
There are 2 algorithms providing output and associated text statistics as follows:
- **Flesch Reading Ease**: 
  - In the Flesch reading-ease test, higher scores indicate material that is easier to read; lower numbers mark passages that are more difficult to read.
  - The formula for the Flesch reading-ease score (FRES) test is:
    - 206.835 - (1.015 * (total words / total sentences)) - (84.6 * (total syllables / total words))
    - The score is a float number rounded to 3 decimal places.
  - Grade level can be permuted from the Flesch Reading Ease score:
    - 100.00–90.00 - 5th grade - Very easy to read. Easily understood by an average 11-year-old student. 
    - 90.0–80.0 - 6th grade	Easy to read - Conversational English for consumers. 
    - 80.0–70.0 - 7th grade - Fairly easy to read. 
    - 70.0–60.0	- 8th & 9th grade - Plain English. Easily understood by 13- to 15-year-old students. 
    - 60.0–50.0	- 10th to 12th grade - Fairly difficult to read. 
    - 50.0–30.0	- College - Difficult to read. 
    - 30.0–10.0	- College graduate - Very difficult to read. Best understood by university graduates. 
    - 10.0–0.0 - Professional - Extremely difficult to read. Best understood by subject-matter experts.
- **Flesch Kincaid Grade Level**:
  - These readability tests are used extensively in the field of education. The "Flesch–Kincaid Grade Level Formula" presents a score as a U.S. grade level, making it easier to assess audience.
  - It can also mean the number of years of education generally required to understand this text, most relevant when the formula results in a number greater than 10.
  - The reason to use the calculated grade level versus the permuted table is when there is potential for text to be outside the minimum and maximum table lookup.
  - Note there is often a difference between the permuted grade level and the calculated grade level.
  - The grade level is calculated with the following formula:
    - (0.39 * (total words / total sentences)) + (11.8 * (total syllables / total words)) -15.59
    - The calculated grade is a float number rounded to 3 decimal places.
- **Text Statistics**:
  - Number of words
  - Number of syllables
  - Number of sentences
- for more info, see this [Wikipedia entry](https://en.wikipedia.org/wiki/Flesch–Kincaid_readability_tests) 

### Validation Text ###
- **Easy:** `The cat sat on the mat.` scores 116 and is considered VERY easy to read with a single sentence of single syllable words. 
  - {'num_sentences': 1, 'num_words': 6, 'num_syllables': 6} {'readability': 116.145, 'read_grade': '5th Grade', 'calc_grade': -1.45} 
  - NOTE the very low calcualted reading grade as compared to the permuted grade level. <br />
- **Low:** `The quick red fox jumped over the lazy brown dog.` is a low grade difficulty sentence scoring 86.705. 
  - {'num_sentences': 1, 'num_words': 10, 'num_syllables': 13} {'readability': 86.705, 'read_grade': '6th Grade', 'calc_grade': 3.65} <br />
- **Mid:** `This sentence, taken as a reading passage unto itself, is being used to prove a point.` has a readability of 69. 
  - {'num_sentences': 1, 'num_words': 16, 'num_syllables': 23} {'readability': 68.983, 'read_grade': '9th Grade', 'calc_grade': 7.613} <br />
- **Hard:** `The Australian platypus is seemingly a hybrid of a mammal and reptilian creature.` possesses a readability of 37.455. 
  - {'num_sentences': 1, 'num_words': 13, 'num_syllables': 24} {'readability': 37.455, 'read_grade': 'College Level', 'calc_grade': 11.265} <br />


### Questions ###
Feel free to contact for questions, comments, concerns or interact directly via the GitHub repository.

Randall Shane PhD<br />
Randall@NumbersAndTech.com<br />
https://github.com/RandallShanePhD/fkscore<br />
Thank you!
