#!/usr/bin/env python

# task 3
import sys
import string
import csv 

for line in sys.stdin:
    
 #Remove leading and trailing whitespace
 line = line.strip()
 #Split line into array of entry data
	
 entry = csv.reader([line])
 for row in entry:
	
  print ('%s\t%s' %(row[2],row[12])) 
