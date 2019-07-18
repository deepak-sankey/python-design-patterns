"""
Author      : Digambar Gadekar
Created At  : 17 July 2019
Description : All utility related services will be here
"""

import json

#JSON
#Reads data from the given json file and returns list/json
def read_json_data(data_source):
   fp = open(data_source, encoding="utf8")
   data = json.loads(fp.read())
   return data
