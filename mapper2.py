#!/usr/bin/env python
import sys

columns = ("vin", "make", "year")

for line in sys.stdin:
    
    # Strip and split line, zip into dictionary
    data = line.strip().split(",")
    data_dict = dict(zip(columns, data))

    # Assign key, value
    make = data_dict["make"]
    year = data_dict["year"]
    
    # Prepare tab and comma separated output
    key = "%s,%s" % (make, year)
    value = 1
    print("%s|%s" % (key, value))
