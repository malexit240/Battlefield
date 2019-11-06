from abc import abstractmethod

from local_random import R

STRATEGIES = {}


def add_to_registry(strategy_name):
    def register(fn):
        STRATEGIES[strategy_name] = fn
        return fn
    return register


def get_squad_with_strategy(name: str, army):
    return STRATEGIES[name](army)


@add_to_registry('random')
def random_choose_squad(army):
    return R.choice(army.squads)


@add_to_registry('weakest')
def weakest_choose_squad(army):
    return min(army.squads)


@add_to_registry('strongest')
def strongest_choose_squad(army):
    return max(army.squads)
