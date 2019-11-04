from abc import abstractmethod

from local_random import R

STRATEGIES = {}


def add_to_registry(strategy_name):
    def decor(fn):
        STRATEGIES[strategy_name] = fn
        return fn
    return decor


def get_unit_with_strategy(name: str, army):
    return STRATEGIES[name](army)


@add_to_registry('random')
def random_choose_unit(army):
    squad = R.choice(army.squads)
    unit = R.choice(squad.units)

    return unit


@add_to_registry('weakest')
def weakest_choose_unit(army):
    return min(min(army.squads).units)


@add_to_registry('strongest')
def strongest_choose_unit(army):
    return max(max(army.squads).units)
