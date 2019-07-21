"""
Author      : Vishal Panchal
Created At  : 17 July 2019
Description : To read the JSON file and return the data
"""

import json

# Author : Vishal Panchal
# Reads data from the given json file and returns list/json
def read_json_data(data_source):
   fp = open(data_source, encoding="utf8")
   data = json.loads(fp.read())
   return data
