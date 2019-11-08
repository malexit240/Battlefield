"""
this module is the start point of the programm
"""

from configuration import CONFIGURATION as Conf
from local_random import R

from units_creator import get_squads, Army
from battlefield import Battlefield

from replay import Logger, LoggerJSON, load_replay_from_JSON
from battle_replay import replay


def main():

    Conf.load('config.json')

    R.seed(Conf.seed)

    armies = list()

    for army_name in Conf.armies:
        armies.append(Army(army_name, get_squads(
            Conf.armies[army_name]), Conf.armies[army_name]['strategy']))

    b = Battlefield(armies)

    b.start_battle()

    console_loger = Logger(replay)
    console_loger.write_all()

    with open('result.json', 'w') as output_file:
        loger = LoggerJSON(replay, output_file)
        loger.write_all()


if(__name__ == '__main__'):
    main()
