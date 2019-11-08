"""
this module contains functions that return divisions with units or subdivisions
"""

from configuration import CONFIGURATION as Conf
from local_random import R
from army import Army
from squad import Squad
from units import Soldier, Vehicles


def get_operators(amount: int) -> list:
    """returns operators instances"""
    operators = list()

    for _ in range(amount):
        operators.append(Soldier(Conf.units['max_soldier_health'], R.randint(
            Conf.units['min_soldier_recharge'], Conf.units['max_soldier_recharge'])))

    return operators


def get_units(amount: int, vehicle_proportion: float, operators_amount: int) -> list:
    """returns units(soldiers and vehicles) instances"""
    units = list()

    for _ in range(amount):
        unit = R.choices([Soldier, Vehicles], weights=[
            1-vehicle_proportion, vehicle_proportion])[0](Conf.units['max_soldier_health'], R.randint(Conf.units['min_soldier_recharge'], Conf.units['max_soldier_recharge']))
        if(isinstance(unit, Vehicles)):
            unit.operators = get_operators(operators_amount)
        units.append(unit)

    return units


def get_squads(army_config: list) -> list:
    """returns squads with units"""
    squads = list()
    for _ in range(int(army_config['squad_amount'])):
        squads.append(
            Squad(get_units(int(army_config['units_per_squad']), float(
                army_config['vehicle_proportion']), int(army_config['operators_in_vehicle_amount']))))

    return squads
