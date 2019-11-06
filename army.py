from army_organization import Division, Subject
from replay import set_id


class Army(Division, Subject):
    """
    Army class
    """

    name: str
    squads: list
    strategy: str

    @set_id
    def __init__(self, name: str, squads: list, strategy: str):
        self.name = name
        self.squads = squads
        self.subjects = self.squads
        self.strategy = strategy

    def on_excluding(self):
        if(len(self.squads) == 0):
            self.up_division.exclude(self)
