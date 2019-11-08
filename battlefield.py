"""
this module contains battlefield class
"""

from local_random import R

from army_organization import Division
from army import Army

from strategy import get_squad_with_strategy as gsws

from battle_replay import replay as replay


class Battlefield(Division):
    """
    Battlefield class

    Contains battle simulation algorithm
    """

    _armies: list

    def __init__(self, armies: list):
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

    def squad_attacks(self, attacker, defender):
        """inflict damage to defender units from attacker units"""

        for unit in attacker.units:
            if(len(defender.units) != 0):
                if(unit.hit):
                    enemy = R.choice(defender.units)
                    enemy.damage_inflicte(unit.beat(enemy))
            else:
                return

    @replay.battle_end
    def start_battle(self):
        """Run battle simulation"""

        while(len(self.armies) > 1):
            (first_army, second_army) = self.get_two_armies()

            first_squad = gsws(second_army.strategy, first_army)
            second_squad = gsws(first_army.strategy, second_army)

            if(first_squad.power < second_squad.power):
                first_squad, second_squad = second_squad, first_squad

            self.squad_attacks(first_squad, second_squad)
            self.squad_attacks(second_squad, first_squad)
