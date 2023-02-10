"""json module is used for storing and exchanging of data
json means javascript object notation"""
"""json to python- json.loads()
   python to json- json.dumps()"""

import json
print(dir(json))

import os
print(dir(os))

import random
print(dir(random))

print("1.json module")
import json

x='{"name":"mrunal","age":25,"course":"python"}' #json
print(type(x))

#parsing json to python
y=json.loads(x)
print(type(y))

#parsing python to json
z={"name":"mrunal","age":25,"course":"python"}
z=json.dumps(x)
print(type(z))