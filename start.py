from configuration import ARMIES_CONFIGURATION as AConf
from configuration import UNITS_CONFIGURATION as UConf
from configuration import SEED as seed
from battlefield import Battlefield
from local_random import R

from army import Army
from squad import Squad
from units import Soldier, Vehicles


def get_operators(amount: int) -> list:
    operators = list()

    for _ in range(amount):
        operators.append(Soldier(UConf['max_soldier_health'], R.randint(
            UConf['min_soldier_recharge'], UConf['max_soldier_recharge'])))

    return operators


def get_units(amount: int, vehicle_proportion: float, operators_amount: int) -> list:
    units = list()

    for _ in range(amount):
        unit = R.choices([Soldier, Vehicles], weights=[
            1-vehicle_proportion, vehicle_proportion])[0](UConf['max_soldier_health'], R.randint(UConf['min_soldier_recharge'], UConf['max_soldier_recharge']))
        if(isinstance(unit, Vehicles)):
            unit.operators = get_operators(operators_amount)
        units.append(unit)

    return units


def get_squads(army_config: list) -> list:
    squads = list()
    for _ in range(int(army_config['squad_amount'])):
        squads.append(
            Squad(get_units(int(army_config['units_per_squad']), float(
                army_config['vehicle_proportion']), int(army_config['operators_in_vehicle_amount']))))

    return squads


def main():

    R.seed(seed)

    armies = list()

    for army_name in AConf:
        armies.append(Army(army_name, get_squads(
            AConf[army_name]), AConf[army_name]['strategy']))

    b = Battlefield(armies)

    b.start_battle()


if(__name__ == '__main__'):
    main()
