#!/bin/python

import textwrap
import fileinput
import sys


LineIn= sys.stdin.readline()
LineOut= textwrap.wrap(LineIn, width=70)          


for k in LineOut:
    k= '"' + k + '"' + ' ' 
    sys.stdout.write(k)
    #    print (k)


    




