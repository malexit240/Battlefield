"""this module contains a Vehicle class"""

from .unit import Unit
from army_organization import Division

from geometric_average import geometric_average as gavg
from local_random import R

from replay import set_id
from battle_replay import replay


class Vehicles(Unit, Division):
    """Vehicle class
    contains operators"""

    def __init__(self, health: int, recharge: int,):
        Unit.__init__(self, health, recharge)
        self.__health = health
        self._operators = list()

    @property
    def health(self) -> float:
        return sum((operator.health
                    for operator in self._operators)) + self.__health

    @health.setter
    @replay.unit_low_health
    def health(self, value):
        self.__health = value

    @property
    def damage(self) -> float:
        return 0.1 + self.experience

    @property
    def attack_probability(self) -> float:
        return 0.5 * (1 + self.__health / 100.0) * gavg([operator.attack_probability
                                                         for operator in self._operators])

    @property
    def power(self) -> float:
        return 0.8 * self.damage + 0.2 * self.health

    @property
    def operators(self) -> list:
        return self._operators

    @operators.setter
    def operators(self, value):
        self._operators = value
        self.subjects = value

    @property
    def experience(self) -> int:
        return sum((operator.experience
                    for operator in self._operators))

    def damage_inflicte(self, damage: int):
        """reduces a vehicle self health on damage value and partially reduces operators health"""

        if(damage == 0):
            return

        self.__health -= 0.6*damage

        looser = R.choice(self._operators)
        looser.damage_inflicte(0.2 * damage)

        for o in self._operators:
            if(o is not looser):
                o.damage_inflicte(0.2/(len(self._operators)-1) * damage)

        if(self.__health <= 0 or looser.health <= 0):
            self.up_division.exclude(self)

    def on_excluding(self):
        """trigger when unit excludes from division
        override the base method of the Division class"""
        if(len(self.operators) == 0):
            self.up_division.exclude(self)

    def beat(self):
        """extends the base method of the Unit class to add experience increase on a successful attack"""

        damage = super().beat()
        if(damage != 0):
            for o in self._operators:
                o.experience += 1
        return damage
