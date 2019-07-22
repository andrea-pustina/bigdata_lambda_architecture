"""
Word count topology
"""

from streamparse import Grouping, Topology

from bolts.pre_process import PreProcessBolt
from bolts.alert import AlertBolt
from bolts.mean_line import MeanByLineBolt
from spouts.msg import MsgSpout


class BusAnalysis(Topology):
    msg_spout = MsgSpout.spec()
    pre_process_bolt = PreProcessBolt.spec(inputs=[msg_spout], par=5)
    alert_bolt = AlertBolt.spec(inputs=[pre_process_bolt], par=5)
    mean_by_line_bolt = MeanByLineBolt.spec(inputs={pre_process_bolt: Grouping.fields("line")}, par=5)
