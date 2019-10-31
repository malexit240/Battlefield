import random as r
from .unit import Unit


class Vehicles(Unit):
    operators: list

    @property
    def damage(self):

        damage = 0
        for o in self.operators:
            damage += o.damage()

        return damage

    @property
    def atack_probability(self):
        return r.random()
