import sys
import json
data = {
    'big number' : 2 * 1024,
    'max float' : sys.float_info.max,
    'a_list' : [i for i in range(5)]
}

json_data = json.dumps(data)
print(json_data)
data_out = str(json.loads(json_data))
print(data_out)
print(json_data == data_out) 

print(type(json_data))
print(type(data_out))