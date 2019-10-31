from random import Random

from configuration import CONFIGURATION as C
from battlefield import Battlefield
from eventual import E

from army import Army
from squad import Squad
from units import Soldier, Vehicles


def get_units(amount: int, vehicle_proportion: float) -> list:
    units = list()

    for _ in range(amount):
        units.append(E.choices([Soldier, Vehicles], weights=[
                     1-vehicle_proportion, vehicle_proportion])[0]())

    return units


def get_squads(army_config: list) -> list:
    squads = list()
    for _ in range(int(army_config['squad_amount'])):
        squads.append(
            Squad(get_units(int(army_config['units_per_squad']), float(army_config['venicle_proportion']))))

    return squads


def main():
    # parse configuration

    E.seed(C['seed'])

    armies = list()

    for name in C['armies']:
        armies.append(Army(name, get_squads(C['armies'][name])))

    print(armies)

    b = Battlefield(armies)

    # create battlefield

    # start battle


if(__name__ == '__main__'):
    main()
