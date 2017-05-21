#!/usr/bin/env python

# task7
import sys
import string
currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
 line = line.strip()
 
 entry = line.split('\t',2)
 key = entry[0]
 dayofweek = entry[1]

	#Parse key/value input (your code goes here)

	#If we are still on the same key...
 if currentkey == key:
  if dayofweek =='wknd':
   wknd_count +=1.00
  else:
   wkdy_count +=1.00
 else:
  if currentkey is not None:
   wknd_avg = '%0.2f' % (float(wknd_count/8.00))
   wkdy_avg = '%0.2f' % (float(wkdy_count/23.00))
   
   print ('%s\t%s, %s' %(currentkey,wknd_avg,wkdy_avg))
  currentkey = key
  wknd_count = 0 
  wkdy_count = 0
  if dayofweek == 'wknd':
   wknd_count +=1.00
  else:
   wkdy_count +=1.00
   
   
 
                
        
if key == currentkey:
 wknd_avg = '%0.2f' % (float(wknd_count/8.00))
 wkdy_avg = '%0.2f' % (float(wkdy_count/23.00))  
 print ('%s\t%s, %s' %(currentkey,wknd_avg,wkdy_avg))
