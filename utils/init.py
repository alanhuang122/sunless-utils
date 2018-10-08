#!/usr/bin/python
import json

data = {}

print('loading...')
with open('sunless.dat') as f:
    for line in f:
        try:
            temp = json.loads(line)
            data[temp['key']] = temp['value']
        except:
            print(line)

import sunless
sunless.data=data
