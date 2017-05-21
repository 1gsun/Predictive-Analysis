#!/usr/bin/env python

# task 2
import sys
import string
import csv 
for line in sys.stdin:
 line = line.strip()
 #Remove leading and trailing whitespace
 entry = csv.reader([line])
	
 for row in entry:

  print (row[2])
