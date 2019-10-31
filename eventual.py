from random import Random

r = Random()
r.seed(0)


class Eventual:
    r: Random

    def __init__(self, seed: int):
        self.r = Random()
        self.r.seed(seed)

    def set_seed(self, seed: int):
        self.r.seed(seed)

    def get_choice(self, seq) -> object:
        return self.r.choice(seq)


E = Random()
