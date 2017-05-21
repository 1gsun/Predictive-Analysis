from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext



if __name__ == "__main__":
 if len(sys.argv) != 2:
  print("Usage: wordcount <file>", file=sys.stderr)
  exit(-1)
 sc = SparkContext()
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x)).map(lambda x:(int(x[2]),1)).reduceByKey(lambda x,y: x+y).sortByKey()
 line =line.map(lambda x: '%s\t%s' %(x[0],x[1]))
 
 line.saveAsTextFile("task2.out") 


 sc.stop()
