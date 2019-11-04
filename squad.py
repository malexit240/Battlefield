from army_organization import Division, Subject
from units.unit import get_attrs_from_objects_list as gafol


class Squad(Division, Subject):
    """Squad class"""
    units: list

    def __init__(self, units):
        self.units = units
        self.subdivision = self.units

    @property
    def power(self) -> float:
        return sum(gafol('power', self.units))

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
        if(len(self.units) == 0):
            self.up_division.exclude(self)
