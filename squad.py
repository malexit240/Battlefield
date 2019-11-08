"""this module contains Squad class"""

from army_organization import Division, Subject
from replay import set_id


class Squad(Division, Subject):
    """Squad class
    contains units"""
    units: list

    @set_id
    def __init__(self, units):
        self.units = units
        self.subjects = self.units

    @property
    def power(self) -> float:
        return sum([unit.power for unit in self.units])

    def __gt__(self, obj):
        try:
            return self.power > obj.power
        except AttributeError:
            print('obj has not attribute "power"')
            raise AttributeError()

    def __lt__(self, obj):
        try:
            return self.power < obj.power
        except AttributeError:
            print('obj has not attribute "power"')
            raise AttributeError()

    def on_excluding(self):
        """overrides Division class base method"""
        if(len(self.units) == 0):
            self.up_division.exclude(self)
