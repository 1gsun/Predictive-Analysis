#!/usr/bin/env python

# task 6
import sys
import string
import csv 

for line in sys.stdin:
    
 #Remove leading and trailing whitespace

 #Split line into array of entry data
	
 entry = csv.reader([line])
 for row in entry:
  print ('%s, %s' %(row[14],row[16])) 
