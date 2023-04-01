#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar
-files mapper.py,reducer.py
-input /user/cloudera/mapreduce/test.txt
-output /user/cloudera/mapreduce/output
-mapper "python mapper.py"
-reducer "python reducer.py"
