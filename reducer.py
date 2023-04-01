#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

total = 0
count = 0
word = 0

# input comes from STDIN
for line in sys.stdin:
 
    line = line.strip()
    word, count_1 = line.split('\t', 1)

   
    word=int(word)
    count = int(count)
    count_1 =int(count_1)            
    
    total=float(word+total) 
    count=float(count+count_1)
    
    avg = float(total/count)

print '%s' % (avg)
