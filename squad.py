from army_organization import Division, Subject



class Squad(Division, Subject):
    """Squad class"""
    units: list

    def __init__(self, units):
        self.units = units
        self.subdivision = self.units

    @property
    def power(self) -> float:
        return sum((unit.power for unit in self.units))
        

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
