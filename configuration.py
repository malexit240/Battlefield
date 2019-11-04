import json


class Configuration:

    seed: int
    armies: dict
    units: dict

    def __init__(self):
        pass

    def load(self, path: str):
        # =============== add with
        json_file = open(path, 'rb') # ==================================== or generate config
        raw = json.load(json_file)
        json_file.close()

        self.seed = int(raw.pop('seed'))

        self.armies = raw.pop('armies')

        self.units = raw.pop('unit_configuration')

        for key in self.units:
            self.units[key] = int(self.units[key])


CONFIGURATION = Configuration()
