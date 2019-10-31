from .unit import Unit
import random as r


class Soldier(Unit):
    experience: int

    @property
    def damage(self):
        return self.experience

    @property
    def atack_probability(self):
        return r.random()
