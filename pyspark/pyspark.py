# Test Pi
import findspark
findspark.init()

import pyspark
import random

sc = pyspark.SparkContext(appName="Pi")
num_samples = 100000000

def inside(p):     
  x, y = random.random(), random.random()
  return x*x + y*y < 1

count = sc.parallelize(range(0, num_samples)).filter(inside).count()

pi = 4 * count / num_samples
print(pi)

sc.stop()











# Read csv
import findspark
findspark.init()

import pyspark
sc=pyspark.SparkContext(appName="fhv")
spark=pyspark.sql.SparkSession(sc)

df=spark.read.csv('C:/Users/mayij/Desktop/fhvhv_tripdata_2020-06.csv',header=True,inferSchema=True)
df.show(5)
df.printSchema()
df.filter(df.hvfhs_license_num=='HV0005').show(2)
df.where((df.hvfhs_license_num=='HV0005')&(df.PULocationID==55)).show(2)
df.registerTempTable('dfsql')
spark.sql('select * from dfsql').show(2)







# Read RDD
import findspark
findspark.init()

import pyspark
sc=pyspark.SparkContext(appName="fhv")

rdd=sc.textFile('hdfs://localhost:9000/fhv/fhvhv_tripdata_2020-06.csv')
rdd.take(10)

# rdd works in jupyter
