#!/usr/bin/env python

# task3
import sys
import string
currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

 #Remove leading and trailing whitespace
 line = line.strip()

 #Get key/value 
    
 entry = line.split('\t',2)
 key = entry[0]
 val = float(entry[1])
    

 #Parse key/value input (your code goes here)

 #If we are still on the same key...
 if currentkey == key:
  current_count += 1 
  current_sum += val
        
 else:
  if currentkey is not None:
   total = "%0.2f" % (float(current_sum))
   avg = "%0.2f" % (float(current_sum/current_count))
   vp = "%s, %s" % (total,avg)
   print ('%s\t%s' %(currentkey,vp))
  current_sum = val 
  current_count = 1 
  currentkey = key
                
if key == currentkey:
 total = "%0.2f" % (float(current_sum))
 avg = "%0.2f" % (float(current_sum/current_count))
 vp = "%s, %s" % (total,avg)
 print ('%s\t%s' %(currentkey,vp))    
	           
