#!/usr/bin/env python
import sys

output_dict = {}

for line in sys.stdin:

    # Split key and value and zip into dict
    data = line.strip().split("|")
    data_dict = dict(zip(["key", "value"], data))

    key = data_dict["key"]
    value = data_dict["value"]

    # Increment accident count by one for each VIN
    if key in output_dict.keys():
        output_dict[key] += 1
    else:
        output_dict[key] = 1
    
for key, value in output_dict.items():
    print("%s,%s" % (key, value))
