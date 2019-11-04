"""
Represents the hierarchical principle in the army
"""

from abc import abstractclassmethod


class Division:
    """Division class"""

    _subdivision: list

    def __init__(self, subdivision: list):
        self._subdivision = subdivision

    @property
    def subdivision(self) -> list:
        return self._subdivision

    @subdivision.setter
    def subdivision(self, value):
        self._subdivision = value
        for sub in self.subdivision:
            if(isinstance(sub, Subject)):
                sub.set_up_division(self)

    def exclude(self, obj):
        if(obj in self.subdivision):
            self.subdivision.remove(obj)
        self.on_excluding()

    @abstractclassmethod
    def on_excluding(self):
        pass


class Subject:
    """Subject class"""
    up_division: Division

    def set_up_division(self, division: Division):
        self.up_division = division
