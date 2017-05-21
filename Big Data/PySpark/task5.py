from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext

#task 5

 
if __name__ == "__main__":
 if len(sys.argv) != 2:
  print("Usage: wordcount <file>", file=sys.stderr)
  exit(-1)
 sc = SparkContext()
 lines = sc.textFile(sys.argv[1], 1)
 line = lines.mapPartitions(lambda x:reader(x)).map(lambda x:((x[14],x[16]),1))
 
 line = line.reduceByKey(add)
 
 line = line.sortBy(lambda x: x[1],False)
 top = line.take(1)
 output = sc.parallelize(top)
 
 line = output.map (lambda x:'%s, %s\t%s' % (x[0][0],x[0][1],x[1]))
 line.saveAsTextFile("task5.out") 


 sc.stop()
