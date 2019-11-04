import json


class Configuration:

    seed: int
    armies: dict
    units: dict

    def __init__(self):
        pass

    def load(self, path: str):
        json_file = open(path, 'rb')
        raw = json.load(json_file)

        self.seed = int(raw.pop('seed'))

        self.armies = raw.pop('armies')

        self.units = raw.pop('unit_configuration')

        for key in self.units:
            self.units[key] = int(self.units[key])


CONFIGURATION = Configuration()
