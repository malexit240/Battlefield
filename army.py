from strategy import Strategy


class Army:
    name: str
    squads: list
    strategy: Strategy

    def __init__(self, name: str, squads: list):
        self.name = name
        self.squads = squads
