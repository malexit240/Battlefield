from .replay import Replay
from json import dumps


class Loger:
    replays: Replay
    out: None

    def __init__(self, replays: Replay, file=None):
        self.replays = replays
        self.out = file

    def write_all(self):
        for event in self.replays.events:
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


class LogerJSON(Loger):
    def __init__(self, replays: Replay, file):
        self.replays = replays
        self.out = file

    def write_all(self):
        self.out.write(dumps([(event.name, event.values)
                              for event in self.replays.events], indent=2))
