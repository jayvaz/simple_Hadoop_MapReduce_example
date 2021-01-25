#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # lowercase text
    line = line.strip().lower()

    # remove punctuation
    import string

    s = line
    table = string.maketrans("","")
    new_line = s.translate(table,string.punctuation)

    # split the line into words; splits on any whitespace
    words = new_line.split()

    # output tuples (word, 1) in tab-delimited format
    from sklearn.feature_extraction import stop_words
    stops = set(stop_words.ENGLISH_STOP_WORDS)

    for word in words:
        if word not in stops:
            print '%s\t%s' % (word, "1")
