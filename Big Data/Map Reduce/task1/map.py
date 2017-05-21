#!/usr/bin/env python

# task1
import sys
import string
import csv 
for line in sys.stdin:
    
 #Remove leading and trailing whitespace
 line = line.strip()

 #Split line into array of entry data
 entry = csv.reader([line])
 for value_list in entry:
  if len(value_list)== 22: # all violations
   print('%s\t%s\t%s, %s, %s, %s' %(value_list[0],1,value_list[14],value_list[6],value_list[2],value_list[1]))
  elif len(value_list)== 18: # open violations
   print ('%s\t%s' %(value_list[0],-1))
  else:
   print ("error")

