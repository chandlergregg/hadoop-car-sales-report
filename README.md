# hadoop-car-sales-report

### About

This repo contains code for the Hadoop car sales report project, an example of using Hadoop MapReduce to process data in HDFS.
This project is part of the Springboard Data Engineering Career Track.

### Details

In this project, we take data on car sales, repairs, and accidents to output a report of the number of accidents by car make and year. This output can be used to determine which cars are accident-prone and used-car buyers can use the output data to inform their car buying decisions.

Hadoop MapReduce is twice:
1. Process input data listing all car sales, repairs and accidents into list of VIN, car make, and year of all cars that had accidents
2. Process data from step 1 into count of accidents by VIN, car make, and year

While MapReduce works best on very large datasets, this project is an example of how to write map and reduce functions in Python, and then run them in HDFS.

##### Data definition of `input_data.csv`
| Column        | Type                                                                |
|---------------|---------------------------------------------------------------------|
| incident_id   | INT                                                                 |
| incident_type | STRING (I: initial sale, A: accident, R: repair)                    |
| vin_number    | STRING                                                              |
| year          | STRING (The year of the car, only populated with incident type “I”) |
| Incident_date | DATE (Date of the incident occurrence)                              |
| description   | STRING                                                              |

### Running locally

To run the map and reduce jobs locally, clone the repo and run the following script in the Mac/Linux command line:
```
cat input_data.csv | ./mapper1.py | sort | ./reducer1.py | ./mapper2.py | sort | ./reducer2.py
```

*Note: Ensure Python 2 or 3 is installed and each mapper and reducer is made executable*

The output will match the data in `output_data.csv`

### Running on HDFS

Hortonworks Sandbox version `2.5.0.0-1245` running on a VirtualBoxVM was used to run the code in HDFS. For details on how to install on your local machine, see instructions [here](https://www.youtube.com/watch?v=735yx2Eak48&ab_channel=BinodSumanAcademy).

##### How to execute MapReduce jobs in HDFS:
1. Copy `input_data.csv` into HDFS as `input.csv`: `/input/data.csv` (You can do this using the Ambari UI)
2. Copy the following files into the VirtualBoxVM running Linux:
  - `mapper1.py`
  - `reducer1.py`
  - `mapper2.py`
  - `reducer2.py`
  - `mapred_jobs.sh`
3. From the root directory in Linux on the VM, run the following:
```
sh mapred_jobs.sh
```

To verify the success of the MapReduce jobs, compare the following files in HDFS with the text files contained in this repo:
  - `/output/all_accidents/part-00000` --> `mapred_1_output.txt`
  - `/output/make_year_count/part-00000` --> `mapred_2_output.txt`
  - `output_data.csv` is just a CSV version of the second MapReduce output with command line stripped away

To see the command line output of running `mapred_jobs.sh`, see `mapred_command_line_output.txt`
