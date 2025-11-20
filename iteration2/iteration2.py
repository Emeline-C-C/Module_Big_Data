from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test My application").getOrCreate()
sc = spark.sparkContext


l = [1, 2, 3, 4, 5]
rdd = sc.parallelize(l)

print(rdd.collect()) #return a list with all RDD element



sc.stop()