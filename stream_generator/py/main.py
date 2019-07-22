import csv
from time import sleep
from json import dumps
from kafka import KafkaProducer
import datetime


speed_multiplier = 60


connected = False
while not connected:
    print("trying to connect to kafka")
    try:
        producer = KafkaProducer(bootstrap_servers=['kafka1:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))
        connected = True
        print("connected to kafka")
    except:
        print("unable to connect to kafka, retrying...")
        sleep(5)
        connected = False

print("starting to send messages")

# '/home/mta_1706.csv', '/home/mta_1708.csv', '/home/mta_1710.csv', '/home/mta_1712.csv'

start_time = datetime.datetime.now()
for path in ['/home/data/mta_1706_sorted']:
    with open(path + '.csv') as csvfile:
        dataset = csv.reader(csvfile)
        first_row = next(dataset)
        first_row_time = datetime.datetime.strptime((first_row[0]), '%Y-%m-%d %H:%M:%S')

        for row in dataset:
            row_time = datetime.datetime.strptime((row[0]), '%Y-%m-%d %H:%M:%S')

                 
            d_time = datetime.datetime.now() - start_time
            d_time = d_time.total_seconds()
            while (d_time < (row_time - first_row_time).total_seconds()/speed_multiplier):
                #print("{} < {} - {}".format(d_time, row_time, first_row_time))
                d_time = datetime.datetime.now() - start_time
                d_time = d_time.total_seconds()
                sleep(1.0)
            #print('send: {}'.format(row))
            producer.send('bus', value=row)


    print('dataset {} finished'.format(path))

print("all datasets finished")
