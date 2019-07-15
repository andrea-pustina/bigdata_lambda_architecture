import csv
from time import sleep
from json import dumps
from kafka import KafkaProducer

msg_per_second = 10

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


for path in ['/home/mta_1706.csv', '/home/mta_1708.csv', '/home/mta_1710.csv', '/home/mta_1712.csv']:
    with open(path) as csvfile:
        dataset = csv.reader(csvfile)
        for row in dataset:
            #print('send: {}'.format(row))
            producer.send('bus', value=row)
            sleep(1.0/msg_per_second)
    print('dataset {} finished'.format(path))

print("all datasets finished")
