from local_random import R
from army_organization import Division, Subject
from .unit_registry import add_id

class Unit(Subject):
    """Unit class"""
    __health: float
    recharge: int  # not used

    @add_id
    def __init__(self, health: float, recharge: int):
        self.__health = health
        self.recharge = recharge

    @property
    def health(self) -> float:
        return self.__health

    @health.setter
    def health(self, value: float):
        self.__health = value
        if(self.__health <= 0):
            self.up_division.exclude(self)

    @property
    def power(self) -> float:
        return self.__health

    @property
    def atack_probability(self) -> float:
        return 0

    @property
    def hit(self) -> bool:
        """return whether attack was successful"""
        return R.random() < self.atack_probability

    def __gt__(self, obj):
        return self.power > obj.power

    def __lt__(self, obj):
        return self.power < obj.power
