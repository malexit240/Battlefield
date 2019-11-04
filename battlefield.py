from army_organization import Division
from army import Army
from strategy import get_unit_with_strategy as guws
from local_random import R


class Battlefield(Division):
    """
    Contains main while
    """

    _armies: list

    def __init__(self, armies: list):
        self.armies = armies

    def shake_armies(self):
        """Change armies order"""

        armies = list()
        while(len(self.armies) != 0):
            armies.append(self.armies.pop(R.randint(0, len(self.armies)-1)))
        self.armies = armies

    @property
    def armies(self):
        return self._armies

    @armies.setter
    def armies(self, value):
        self._armies = value
        self.subdivision = self._armies

    def get_two_armies(self) -> tuple:
        """returns two random armies"""

        if(len(self.armies) < 2):
            print("Could not choose an army. must have more than one army on the list")
            raise Exception

        while(True):
            first = R.randint(0, len(self.armies)-1)
            second = R.randint(0, len(self.armies)-1)

            if(first != second):
                break

        return (self.armies[first], self.armies[second])

    def start_battle(self):
        """Run battle simulation"""
        self.shake_armies()

        while(len(self.armies) > 1):
            (first_army, second_army) = self.get_two_armies()
            first_unit = guws(second_army.strategy, first_army)
            second_unit = guws(first_army.strategy, second_army)

            if(first_unit.hit):
                second_unit.damage_inflicte(first_unit.damage)
            if(second_unit.health > 0 and second_unit.hit):
                first_unit.damage_inflicte(second_unit.damage)

        print(self.armies[0].name)
