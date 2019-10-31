from abc import abstractmethod


class Strategy:

    @abstractmethod
    def choose_unit(self):
        pass


class RandomStrategy(Strategy):
    def choose_unit(self):
        pass
