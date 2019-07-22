from pykafka import KafkaClient

client = KafkaClient(hosts="kafka1:9092")

topic = client.topics['bus']

consumer = topic.get_simple_consumer()
for message in consumer:
  if message is not None:
    print(message.offset, message.value)
