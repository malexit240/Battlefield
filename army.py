"""
Contains army class
"""

from army_organization import Division, Subject


class Army(Division, Subject):
    """
    Army class

    contains squads
    """

    name: str
    squads: list
    strategy: str

    def __init__(self, name: str, squads: list, strategy: str):
        self.name = name
        self.squads = squads
        self.subjects = self.squads
        self.strategy = strategy

    def on_excluding(self):
        """overrides Division class base method"""
        if(len(self.squads) == 0):
            self.up_division.exclude(self)
