#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

total = None
count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count_1 = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        word=int(word)
        count = int(count)
            
	      
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    total=word+total 
    count=count+count_1

print '%s' % (total/count)
