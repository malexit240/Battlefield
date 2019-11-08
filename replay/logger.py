"""this module contains logger classes for printing replays to 
console(Logger object without set file attribute)
text file(Logger object with set file attribute)
json file(LoggerJSON)
"""

from .replay import Replay
from json import dumps


class Logger:
    """Logger class that allows print all events
     from repaly object to console or file"""

    replay: Replay
    out: None

    def __init__(self, replays: Replay, file=None):
        self.replay = replays
        self.out = file

    def write_all(self):
        """write all events from replay to console or file (if file attribute was set)"""

        for event in self.replay.events:
            if(event.name == 'attacks'):
                print(
                    'юнит {} наносит юниту {} {} единиц урона'.format(*event.values), file=self.out)
            elif(event.name == 'unit_destroy'):
                print(
                    'юнит {} уничтожен'.format(*event.values), file=self.out)
            elif(event.name == 'squad_destroy'):
                print(
                    'отряд {} уничтожен'.format(*event.values), file=self.out)
            elif(event.name == 'army_destroy'):
                print(
                    'армия {} уничтожена'.format(*event.values), file=self.out)
            elif(event.name == 'army_win'):
                print(
                    'армия {} победила'.format(*event.values), file=self.out)


class LoggerJSON(Logger):
    """override Logger class to allow write replays to file in json fromat"""

    def __init__(self, replays: Replay, file):
        self.replays = replays
        self.out = file

    def write_all(self):
        """write all events to file in json format
        override method from Logger class
        """

        self.out.write(dumps([(event.name, event.values)
                              for event in self.replays.events], indent=2))
