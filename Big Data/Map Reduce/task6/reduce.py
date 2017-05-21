#!/usr/bin/env python

# task6
import sys
import string

currentkey = None
current_max_count = 0
plate = dict()
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
   plate[currentkey] = current_count

  current_count= 1
  currentkey = line
             
        
if line == currentkey:
 plate[currentkey] = current_count


for i in sorted(plate, key=plate.get,reverse=True)[:20]:
 print ('%s\t%s' %(i,plate[i]))
    

	           
