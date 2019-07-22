import collections
import statistics as stats
from streamparse import Bolt
from pykafka import KafkaClient


class MeanByLineBolt(Bolt):
    outputs = ['line', 'mean_delay']

    def initialize(self, conf, ctx):
        client = KafkaClient(hosts="kafka1:9092")
        topic = client.topics['line_mean_delay']

        self.producer = topic.get_producer()
        self.windows = dict()

    def calculate_mean(self, line, delay):
        if line not in self.windows.keys():
            self.windows[line] = collections.deque(maxlen=10)    #window's size = 10
        self.windows[line].append(delay)
        #self.logger.info("Window for line {}: {}".format(line, self.windows[line]))
        return stats.mean(self.windows[line])

    def process(self, tup):
        line = tup.values[1]
        delay = tup.values[6]
        mean_delay = str(self.calculate_mean(line, int(delay)))
        self.producer.produce('{}, {}'.format(line, mean_delay).encode())
        #self.logger.info("Mean delay for line {}: {}".format(line, mean_delay))
        #self.emit([line, mean_delay])
