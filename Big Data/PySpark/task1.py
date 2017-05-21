from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext

#task 1

def info(x):
 if len(x)== 22:
  return (x[0],[x[14],x[6],x[2],x[1]])
 else:
  return (x[0],"OPEN")

if __name__ == "__main__":

 sc = SparkContext()
 
 first = sc.textFile(sys.argv[1], 1)
 second = sc.textFile(sys.argv[2], 1)
 lines = first.union(second)
 line = lines.mapPartitions(lambda x:reader(x)).map(lambda x:info(x))
 
 line = line.map(lambda nameTuple: (nameTuple[0], [nameTuple[1]])) #convert the value to a list
 line = line.reduceByKey(lambda a, b: a + b) # append the list
 line = line.filter(lambda x: len(x[1])==1) # if there is an open case, the length should be greater than 1 
 line = line.filter(lambda x: x[1][0]!="OPEN") # remove cases only showed up in open but not parking
 line = line.sortByKey()
 out = line.map(lambda x:'%s\t%s, %s, %s, %s' % (x[0],x[1][0][0],x[1][0][1],x[1][0][2],x[1][0][3]))
 
 out.saveAsTextFile("task1.out") 

 sc.stop()

