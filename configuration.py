import json

json_file = open('config.json', 'rb')

CONFIGURATION = json.load(json_file)
