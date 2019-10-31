from army import Army


class Battlefield:
    """
    Contains main while
    """

    armies: list

    def __init__(self, armies: list):
        self.armies = armies

    def start_battle(self):
        while(False):
            for a in self.armies:
                for s in a.squads:
                    for _____ in s.units:
                        pass
