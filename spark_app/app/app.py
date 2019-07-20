from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('bigdata')
sc = SparkContext(conf=conf)

# do something to prove it works
rdd = sc.parallelize(range(100000000))
rdd.sumApprox(3)
