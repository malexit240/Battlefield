"""this module contains Event class and Replay class.
It need to saving battle simulation events
"""

from json import load


class Event:
    """
    Event class

    contains info about battle event

    """

    name: str
    values: list

    def __init__(self, name: str, values: list):
        self.name = name
        self.values = values


# Events in battle:
#
#  name value1 value2...
#
# attacks unit1.id unit2.id unit1.damage
# unit_destroy unit.id
# squad_destroy squad.id
# army_destroy army.name
# army_win army.name


class Replay:
    """
    Replay class

    contains list of events and methods-decorators allows attaches to 'real' battle logic

    """

    events: list

    def __init__(self):
        self.events = list()

    def unit_attacks(self, fn):
        """this method expecting unit instance with _id attribute 
         and decorator can be attach to Unit.beat method or similar"""

        def wrapper(*args, **kwargs):
            units = [unit
                     for unit in args
                     if(hasattr(unit, '_id') and hasattr(unit, 'damage'))
                     ]
            result = fn(*args, **kwargs)

            self.events.append(
                Event('attacks', [units[0]._id, units[1]._id, units[0].damage]))

            return result
        return wrapper

    def unit_low_health(self, fn):
        def wrapper(unit, health):
            if(health <= 0):
                self.events.append(Event('unit_destroy', [unit._id]))

            return fn(unit, health)
        return wrapper

    def division_destroy(self, fn):
        def wrapper(division, subj):
            if(len(division.subjects) == 1):
                if(hasattr(division, 'name')):
                    self.events.append(Event('army_destroy', [division.name]))
                else:
                    self.events.append(
                        Event('squad_destroy', [division._id]))
            result = fn(division, subj)
            return result
        return wrapper

    def battle_end(self, fn):
        def wrapper(battlefield):
            result = fn(battlefield)

            if(hasattr(battlefield, 'armies')):
                self.events.append(
                    Event('army_win', [battlefield.armies[0].name]))

            return result
        return wrapper


def load_replay_from_JSON(file_path: str) -> Replay:
    """
    return replay instance with     
    """
    replay = Replay()
    with open(file_path, 'r') as file:
        events = load(file)

        for event in events:
            replay.events.append(Event(event[0], event[1]))
    return replay
