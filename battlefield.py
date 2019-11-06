from army_organization import Division
from army import Army
from strategy import get_squad_with_strategy as gsws
from local_random import R
from replay import Loger as loger


class Battlefield(Division):
    """
    Contains main while
    """

    _armies: list

    def __init__(self, armies: list):
        self._armies = armies

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
        self.subjects = self._armies

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

    def squad_attacks(self, first, second):
        for unit in first.units:
            if(len(second.units) != 0):
                if(unit.hit):
                    enemy = R.choice(second.units)
                    enemy.damage_inflicte(unit.beat(enemy))
            else:
                return

    def start_battle(self):
        """Run battle simulation"""
        self.shake_armies()

        while(len(self.armies) > 1):
            (first_army, second_army) = self.get_two_armies()

            first_squad = gsws(second_army.strategy, first_army)
            second_squad = gsws(first_army.strategy, second_army)

            if(first_squad.power < second_squad.power):
                first_squad, second_squad = second_squad, first_squad

            self.squad_attacks(first_squad, second_squad)
            self.squad_attacks(second_squad, first_squad)

        print(f" \x1b[31m  Выиграла {self.armies[0].name} армия \x1b[37m")
