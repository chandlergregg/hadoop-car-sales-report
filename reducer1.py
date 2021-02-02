#!/usr/bin/env python
import sys

columns = ("vin", "incident_type", "make", "year")

vin_dict = {}
output_list = []

for line in sys.stdin:

    # Split key and value and zip into dict
    data = line.strip().split("|")
    data_dict = dict(zip(["key", "value"], data))
    
    # Parse key and values
    vin = data_dict["key"]
    value = tuple(data_dict["value"].rstrip().split(","))
    incident_type, make, year = value

    if incident_type == "I":
        vin_dict[vin] = "%s,%s" % (make, year)
    elif incident_type in ("A"):
        output_list.append(vin)

for item in output_list:
    print("%s,%s" % (item, vin_dict[item]))
