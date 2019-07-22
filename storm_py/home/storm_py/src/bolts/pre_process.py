from datetime import datetime
from streamparse import Bolt


class PreProcessBolt(Bolt):
    outputs = ['time', 'line', 'vehicle', 'latitude', 'longitude', 'next_stop', 'delay']

    #def initialize(self, conf, ctx):
        #pass

    def process(self, tup):
        msg = tup.values[0]
        #self.logger.info('==================={}'.format(msg))
        fields = list(map( (lambda s: s.replace('"','').strip()), msg.split(',')))
        #self.logger.info('==================={}'.format(fields))

        time = fields[0]
        line = fields[2]
        vehicle = fields[9]
        latitude = fields[10]
        longitude = fields[11]
        next_stop = fields[12]
           
        try:
            expected_time_s = fields[15].split(' ')[1]
            expected_time = datetime.strptime(expected_time_s, '%H:%M:%S') 
            scheduled_time_s = fields[16]
            s_hours, s_minutes, s_seconds = scheduled_time_s.split(':')
                
            if int(s_hours)>24:
                s_hours = str(int(s_hours)-24)

            scheduled_time = datetime.strptime('{}:{}:{}'.format(s_hours, s_minutes, s_seconds), '%H:%M:%S') 
            delay = (expected_time - scheduled_time).total_seconds()
            #self.logger.info('{}, {}, {}, {}, {}, {}, {}'.format(time, line, vehicle, latitude, longitude, next_stop, delay))         
            self.emit([time, line, vehicle, latitude, longitude, next_stop, delay])
        except:
            pass
