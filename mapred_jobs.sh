#!/bin/bash
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /home/hdfs/mapper1.py -mapper /home/hdfs/mapper1.py \
-file /home/hdfs/reducer1.py -reducer /home/hdfs/reducer1.py \
-input /input/data.csv \
-output /output/all_accidents

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /home/hdfs/mapper2.py -mapper /home/hdfs/mapper2.py \
-file /home/hdfs/reducer2.py -reducer /home/hdfs/reducer2.py \
-input /output/all_accidents \
-output /output/make_year_count