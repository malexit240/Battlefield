"""
Represents the hierarchical principle in the army
"""

from battle_replay import replay


class Division:
    """Division class"""

    _subjects: list

    def __init__(self, subjects: list):
        self._subjects = subjects

    @property
    def subjects(self) -> list:
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        self._subjects = value
        for sub in self.subjects:
            if(isinstance(sub, Subject)):
                sub.set_up_division(self)

    @replay.division_destroy
    def exclude(self, subj):
        if(subj in self.subjects):
            self.subjects.remove(subj)
        self.on_excluding()

    def on_excluding(self):
        pass


class Subject:
    """Subject class"""
    up_division: Division

    def set_up_division(self, division: Division):
        self.up_division = division
