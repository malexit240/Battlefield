from statistics import mean

from .unit import Unit
from army_organization import Division
from local_random import R

class Vehicles(Unit, Division):
    """Vehicle class"""

    def __init__(self, health: int, recharge: int,):
        Unit.__init__(self, health, recharge)
        self.__health = health
        self._operators = list()

    @property
    def health(self) -> float:
        return sum((operator.health for operator in self._operators)) + self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self) -> float:
        return 0.1 + self.experience / 100.0

    @property
    def atack_probability(self) -> float:
        return 0.5 * (1 + self.__health / 100.0) * mean((operator.atack_probability for operator in self._operators))

    @property
    def power(self) -> float:
        return 0.8 * self.damage + 0.2 * self.health

    @property
    def operators(self) -> list:
        return self._operators

    @operators.setter
    def operators(self, value):
        self._operators = value
        self.subdivision = value

    @property
    def experience(self) -> int:
        return sum((operator.experience for operator in self._operators))

    def damage_inflicte(self, damage: int):

        self.__health -= 0.6*damage

        looser = R.choice(self._operators)
        looser.damage_inflicte(0.2 * damage)

        for o in self._operators:
            if(o is not looser):
                o.damage_inflicte(0.2/(len(self._operators)-1) * damage)

        if(self.__health <= 0 or looser.health <= 0):
            self.up_division.exclude(self)

    def on_excluding(self):
        if(len(self.operators) == 0):
            self.up_division.exclude(self)

    @property
    def hit(self) -> bool:
        isHit = R.random() < self.atack_probability
        if(isHit):
            for o in self._operators:
                o.experience += 1
        return isHit
