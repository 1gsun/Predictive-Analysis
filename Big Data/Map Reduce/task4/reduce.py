#!/usr/bin/env python

# task4
import sys
import string
currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

 #Remove leading and trailing whitespace
 line = line.strip()

 #Get key/value   

 #Parse key/value input (your code goes here)

 #If we are still on the same key...
 if currentkey == line:
  current_count += 1
 else:
  if currentkey is not None:
   print ('%s\t%s' %(currentkey,current_count))

  current_count= 1
  currentkey = line
             
        
if line == currentkey:
    
 print ('%s\t%s' %(currentkey,current_count))
