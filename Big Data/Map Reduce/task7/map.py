#!/usr/bin/env python

# task 7
import sys
import string
import csv 

weekend = ['2016-03-05','2016-03-06','2016-03-12','2016-03-13','2016-03-19','2016-03-20','2016-03-26','2016-03-27']
for line in sys.stdin:
    
 #Remove leading and trailing whitespace

 #Split line into array of entry data
	
 entry = csv.reader([line])
 for row in entry:
  if row[1] in weekend:
   print ('%s\t%s' %(row[2],"wknd")) 
  else:
   print ('%s\t%s' %(row[2],"wkdy")) 
