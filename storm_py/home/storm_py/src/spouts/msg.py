from streamparse import Spout
from pykafka import KafkaClient


class MsgSpout(Spout):
    outputs = ['msg']

    def initialize(self, stormconf, context):
        client = KafkaClient(hosts="kafka1:9092")

        topic = client.topics['bus']

        self.simple_consumer = topic.get_simple_consumer()

        #self.balanced_consumer = topic.get_balanced_consumer(
        #    consumer_group=b"test_group",
        #    auto_commit_enable=True,
        #    zookeeper_connect="zookeeper:2181"
        #)
        #self.reg = self.regex()

    def next_tuple(self):
        #message = self.balanced_consumer.consume(block=False)

        message = self.simple_consumer.consume()
        msg = message.value.decode('utf-8').strip('[]')

        if message:
            self.emit([msg])

