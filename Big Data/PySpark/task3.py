from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext

#task 3

if __name__ == "__main__":
 if len(sys.argv) != 2:
  print("Usage: wordcount <file>", file=sys.stderr)
  exit(-1)
 sc = SparkContext()
 lines = sc.textFile(sys.argv[1], 1)
 lines = lines.mapPartitions(lambda x:reader(x)).map(lambda x:(x[2],float(x[12])))
 countsByKey = sc.broadcast(lines.countByKey()) 
 lines = lines.reduceByKey(add).sortByKey() 
 lines = lines.map(lambda x: '%s\t%0.2f, %0.2f' %(x[0],x[1],x[1]/countsByKey.value[x[0]]))  
 lines.saveAsTextFile("task3.out") 


 sc.stop()

