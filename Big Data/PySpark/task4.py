from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext

#task 4

def state(x):
 if x == "NY":
  return ("NY",1)
 else:
  return ("Other",1)
 


if __name__ == "__main__":
 if len(sys.argv) != 2:
  print("Usage: wordcount <file>", file=sys.stderr)
  exit(-1)
 sc = SparkContext()
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x)).map(lambda x:x[16])
 line = line.map(lambda x: state(x))
 line = line.reduceByKey(add)
 line = line.map (lambda x:'%s\t%s' % (x[0],x[1]))
 line.saveAsTextFile("task4.out") 


 sc.stop()
