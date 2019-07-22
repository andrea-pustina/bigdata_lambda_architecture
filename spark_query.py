from pyspark import SparkContext, SparkConf
from datetime import datetime

conf = SparkConf()
conf.setAppName('bigdata')
conf.setMaster('spark://spark-master:7077')

sc = SparkContext.getOrCreate(conf=conf)

dataset = sc.textFile("hdfs://namenode:9000/user/a/test_hdfs.csv")

def split_fields(line):
    msg = line.strip('[]')
    fields = list(map( (lambda s: s.replace('"','').strip()), msg.split(',')))
    time = datetime.strptime(fields[0], '%Y-%m-%d %H:%M:%S')
    day = time.day
    hour = time.hour
    line = fields[2]
    expected_time = fields[15]
    scheduled_time = fields[16]

    return ('{}|{}|{}'.format(day, hour, line)), [expected_time, scheduled_time] 

def calculate_delay(times):
    expected_time = datetime.strptime(times[0].split(' ')[1], '%H:%M:%S')
    s_hours, s_minutes, s_seconds = times[1].split(':')
    if int(s_hours)>=24:
        s_hours = str(int(s_hours)-24)

    scheduled_time = datetime.strptime('{}:{}:{}'.format(s_hours, s_minutes, s_seconds), '%H:%M:%S') 

    delay = (expected_time - scheduled_time).total_seconds()
    return delay


def init():
    return {'sum': 0, 'count': 0}


def compare(acc, delay):
    acc['sum'] += float(delay)
    acc['count'] += 1
    return acc


def combine(acc1, acc2):
    acc1['sum'] += acc2['sum']
    acc1['count'] += acc2['count']
    return acc1


def calculate_mean_delay(acc):
    return acc['sum']/acc['count']

mean_delay_by_line_hour = dataset \
    .map(split_fields) \
    .filter(lambda ticker_values: ticker_values[1][0] != 'NA' and ticker_values[1][1] != 'NA') \
    .mapValues(calculate_delay) \
    .aggregateByKey(init(), compare, combine) \
    .mapValues(calculate_mean_delay)

#print(mean_delay_by_line_hour.collect()[0:10])
            
mean_delay_by_line_hour.saveAsTextFile('hdfs://namenode:9000/user/a/out')

