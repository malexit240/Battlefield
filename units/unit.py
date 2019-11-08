"""this module contains a Unit class
and function that returns current system time in ms"""

from time import time as current_time

from local_random import R
from army_organization import Division, Subject

from replay import set_id
from battle_replay import replay


def current_time_ms():
    """returns current system time in milliseconds"""
    return current_time() * 1000


class Unit(Subject):
    """Base unit class"""

    __health: float
    recharge_time: int  # in milliseconds
    attack_availability_time: int

    @set_id
    def __init__(self, health: float, recharge: int):
        self.__health = health
        self.recharge_time = recharge
        self.attack_availability_time = current_time_ms()

    @property
    def health(self) -> float:
        return self.__health

    @health.setter
    @replay.unit_low_health
    def health(self, value: float):
        self.__health = max(0, value)
        if(self.__health <= 0):
            self.up_division.exclude(self)

    @property
    def power(self) -> float:
        return self.__health

    @property
    def attack_probability(self) -> float:
        return 0

    @replay.unit_attacks
    def beat(self, other_unit) -> float:
        """if attack was successful returns damage value 
        else return zero"""

        if(self.attack_availability_time > current_time_ms()):
            return 0.0

        self.attack_availability_time = current_time_ms() + self.recharge_time

        if(self.hit):
            return self.damage
        else:
            return 0.0

    @property
    def hit(self) -> bool:
        """return whether attack was successful"""
        return R.random() < self.attack_probability

    @property
    def damage(self) -> float:
        return 0.0

    def __gt__(self, obj):
        return self.power > obj.power

    def __lt__(self, obj):
        return self.power < obj.power
