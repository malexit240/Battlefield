from army_organization import Division, Subject


class Army(Division, Subject):
    """
    Army class
    """

    name: str
    squads: list
    strategy: str

    def __init__(self, name: str, squads: list, strategy: str):
        self.name = name
        self.squads = squads
        self.subdivision = self.squads
        self.strategy = strategy

    def on_excluding(self):
        if(len(self.squads) == 0):
            self.up_division.exclude(self)
