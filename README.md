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
  * score['grade']        # Permuted F-K Grade Reading Level

### Releases ###
Releases and additions will push to PyPi periodically, but if there is a feature in master not built/pushed and you want it to be, just ping me.

### History ###
This is a maintained as an implementation of the Flesch-Kincaid readability algorithm which was initially developed in 1948 by Rudolph Flesch and later revised by the U.S. Navy in 1975.  This module is pure python and works with 3.5+.

### Questions ###
Feel free to ping for questions, comments, concerns or interact directly via the GitHub repository.

Randall Shane PhD<br />
Randall@NumbersAndTech.com<br />
https://github.com/RandallShanePhD/fkscore<br />
Thank you!
