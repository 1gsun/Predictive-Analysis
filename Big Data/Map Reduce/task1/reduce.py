#!/usr/bin/env python

#task1

import sys
import string
currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

 #Remove leading and trailing whitespace
 line = line.strip()

 #Get key/value 
 try:
  entry = line.split('\t',3)
  key = entry[0]
  val = int(entry[1])
  info = entry[2]

 except:
  entry = line.split('\t',2)
  key = entry[0]
  val = int(entry[1]) 
  
 if currentkey == key:
  current_sum+= val
 
  if val == 1:
   info_print = info
 
 else:
  if currentkey is not None:

   if current_sum == 1:
    print ('%s\t%s' % (currentkey,info_print))
  current_sum = val 
  currentkey = key
  if val == 1:
   info_print = info 
if key == currentkey:
 if current_sum ==1:
  print ('%s\t%s' %(currentkey,info_print))


	           
