"""
Author      : Digambar Gadekar
Created At  : 17 July 2019
Description : All utility related services will be here
"""

import json
import os

#JSON
#Reads data from the given json file and returns list/json
def read_json_data(data_source):
   fp = open(data_source, encoding="utf8")
   data = json.loads(fp.read())
   return data

def write_json_data(destination_file, data_source):
   with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), destination_file), 'w') as json_file:
      json.dump(data_source, json_file)
   return