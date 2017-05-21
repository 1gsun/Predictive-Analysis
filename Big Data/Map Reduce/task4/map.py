#!/usr/bin/env python

# task 4
import sys
import string
import csv 

for line in sys.stdin:
    
 #Remove leading and trailing whitespace
 line = line.strip()
 #Split line into array of entry data
	
 entry = csv.reader([line])
 for row in entry:
  if row[16] == "NY":
	    
   print ("NY") 
  else:
   print ("Other")
