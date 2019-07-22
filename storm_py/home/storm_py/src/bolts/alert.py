from streamparse import Bolt
from pykafka import KafkaClient


class AlertBolt(Bolt):
    outputs = ["vehicle", "delay"]

    def initialize(self, conf, ctx):
        client = KafkaClient(hosts="kafka1:9092")
        topic = client.topics['delay_alerts']

        self.producer = topic.get_producer()
        self.threshold = 600        #threshold = 10 minutes

    def process(self, tup):
        delay = tup.values[6]
        vehicle = tup.values[2]

        if (int(delay) > self.threshold):
            self.producer.produce('{}, {}'.format(vehicle, delay).encode())
            #self.logger.info("Alert: vehicle {} has a {} seconds delay!".format(vehicle, delay))
            #self.emit([vehicle, delay])
