from .unit import Unit
from local_random import R


class Soldier(Unit):
    """Soldier class"""
    _experience: int

    def __init__(self, health: int, recharge: int):
        super().__init__(health, recharge)
        self._experience = 0

    @property
    def experience(self) -> int:
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = min(value, 50)

    @property
    def damage(self) -> float:
        return 0.05 + self.experience

    @property
    def attack_probability(self) -> float:
        return 0.5 * (1+self.health/100.0) * R.randint(49+self.experience, 100)/100.0

    @property
    def power(self) -> float:
        return 0.8 * self.experience + 0.2 * self.health

    def damage_inflicte(self, damage: int):
        if(damage == 0):
            return

        self.health -= damage

    def beat(self, other_unit: Unit):
        damage = super().beat(other_unit)
        if(damage != 0):
            self.experience += 1
        return damage
