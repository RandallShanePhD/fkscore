fkscore
====

Flesch Kincaid readability score for text

A Python module implementation of the Flesch Kincaid readability score algorithm.

The source code is released under the MIT License.

### Installation ###
    pip install fkscore #or pip3
    requires pyphen 0.9.5+
    requires re

### Usage ###
For text in python represented as a string.

Takes text as string datatype.  Words can be on same or different lines.  This should support all languages under utf-8, but the algorithm is mostly for English language data.  Please validate the results of and report any issues with non-english languages, as they haven't been thoroughly tested.  Email for support, happy to work on these with you.

    import fkscore
    text = '...blah blah blah...'
    f = fkscore(text)
    print(f.stats)
    print(f.score)

### Output ###
Output includes 2 dictionaries of information as follows:
    stats:
        stats['num_words']
        stats['num_syllables']
        stats['num_sentences']
    score:
        score['readability']  # Calculated F-K Readability Score
        score['grade']        # Permuted F-K Grade Reading Level

### Releases ###
Releases and additions will push to PyPi periodically, but if there is a feature in master not built/pushed and you want it to be, just ping me.

### Credit ###
This is a maintained as an original implementation of the Flesch-Kincaid readability score algorithm which has been around since 18...(something).  The module is pure python and works with 3.5+.

### Questions ###
feel free to ping for questions, comments, concerns or hit the repository.
Randall Shane, PhD
Randall.Shane@CodeIntelligence.IO
https://github.com/RandallShanePhD/fkscore
Thank you!
