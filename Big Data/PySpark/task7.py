from __future__ import print_function

import sys
from operator import add
from csv import reader 
from pyspark import SparkContext

#task 7

def wknd(x):
 weekend = ['2016-03-05','2016-03-06','2016-03-12','2016-03-13','2016-03-19','2016-03-20','2016-03-26','2016-03-27']
 if x[1] in weekend:
  return (int(x[0]),1)
 else:
  return (int(x[0]),0)
def wkdy(x):
 weekend = ['2016-03-05','2016-03-06','2016-03-12','2016-03-13','2016-03-19','2016-03-20','2016-03-26','2016-03-27']
 if x[1] not in weekend:
  return (int(x[0]),1)
 else:
  return (int(x[0]),0)


if __name__ == "__main__":
 if len(sys.argv) != 2:
  print("Usage: wordcount <file>", file=sys.stderr)
  exit(-1)
 sc = SparkContext()
 
 lines = sc.textFile(sys.argv[1], 1)
 wknd = lines.mapPartitions(lambda x:reader(x)).map(lambda x:(x[2],x[1])).map(lambda x: wknd(x)).reduceByKey(add)
 wkdy = lines.mapPartitions(lambda x:reader(x)).map(lambda x:(x[2],x[1])).map(lambda x: wkdy(x)).reduceByKey(add)

 output = wknd.leftOuterJoin(wkdy).sortByKey()
 out = output.map(lambda x:'%s\t%0.2f, %0.2f' % (x[0],float(x[1][0]/8.00),float(x[1][1]/23.00)))
 
 out.saveAsTextFile("task7.out") 


 sc.stop()

