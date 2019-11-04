import json

json_file = open('config.json', 'rb')

RAW_CONFIGURATION = json.load(json_file)

ARMIES_CONFIGURATION = RAW_CONFIGURATION.pop('armies')
SEED = int(RAW_CONFIGURATION.pop('seed'))


UNITS_CONFIGURATION = RAW_CONFIGURATION.pop('unit_configuration')

for key in UNITS_CONFIGURATION:
    UNITS_CONFIGURATION[key] = int(UNITS_CONFIGURATION[key])

del RAW_CONFIGURATION
