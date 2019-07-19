import csv
from time import sleep
import datetime

# './mta_1706', './mta_1708', './mta_1710', './mta_1712'

for path in ['./data/mta_1706']:
    with open(path + '.csv') as infile:
        with open(path + '_sorted.csv', mode='w') as out_file:
	    
            print("file: {}".format(path))
            
            print("\tloading input... ", end='', flush=True)
            dataset = csv.reader(infile)
            dataset = list(dataset)[1:]
            print("ok")
            
            print("\tsorting... ", end='', flush=True)
            dataset.sort(key=lambda s: datetime.datetime.strptime((s[0]), '%Y-%m-%d %H:%M:%S'))
            print("ok")
            
            print("\twriting output... ", end='', flush=True)
            writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(dataset)
            print("ok")


print("all datasets finished")
