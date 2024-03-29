"""
Author      : Vishal Panchal
Created At  : 17 July 2019
Description : To read and write the JSON file
"""

import json
import os

# Author : Vishal Panchal
# Reads data from the given json file and returns list/json
def read_json_data(data_source):
   fp = open(data_source, encoding="utf8")
   data = json.loads(fp.read())
   return data

#Writes data to the given json file
def write_json_data(destination_file, data_source):
   with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), destination_file), 'w') as json_file:
      json.dump(data_source, json_file)
   return
