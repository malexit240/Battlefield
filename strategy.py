"""this module contains list of available strategies"""

from abc import abstractmethod

from local_random import R

STRATEGIES = {}


def add_to_registry(strategy_name):
    """registres a strategy function as available"""
    def register(fn):
        STRATEGIES[strategy_name] = fn
        return fn
    return register


def get_squad_with_strategy(name: str, army):
    """returns a strategy function by name"""
    return STRATEGIES[name](army)


@add_to_registry('random')
def random_choose_squad(army):
    """returns a random squad from army"""
    return R.choice(army.squads)


@add_to_registry('weakest')
def weakest_choose_squad(army):
    """returns a weakest squad from army"""
    return min(army.squads)


@add_to_registry('strongest')
def strongest_choose_squad(army):
    """returns a strongest squad from army"""
    return max(army.squads)
