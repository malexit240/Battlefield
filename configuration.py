import json


class Configuration:
    """
    Configuration class

    contains information for units+ instantiation
    and seed for randomizer
    """

    seed: int
    armies: dict
    units: dict

    def __init__(self):
        pass

    def load(self, file_path: str):
        """
        fills attributes from configuration file
        """

        json_file = open(file_path, 'rb')
        raw = json.load(json_file)
        json_file.close()

        self.seed = int(raw.pop('seed'))

        self.armies = raw.pop('armies')

        self.units = raw.pop('unit_configuration')

        for key in self.units:
            self.units[key] = int(self.units[key])


CONFIGURATION = Configuration()
