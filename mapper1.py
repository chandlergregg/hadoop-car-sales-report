#!/usr/bin/env python
import sys

columns = ("incident_id", "incident_type", "vin", "make", "model", "year", "incident_date", "description")

for line in sys.stdin:
    
    # Strip and split line, zip into dictionary
    data = line.strip().split(",")
    data_dict = dict(zip(columns, data))

    # Assign key, value
    key = data_dict["vin"]
    value = "%s,%s,%s" % (data_dict["incident_type"], data_dict["make"], data_dict["year"])
    
    # Prepare tab and comma separated output
    output = "%s|%s" % (key, value)
    print(output)
