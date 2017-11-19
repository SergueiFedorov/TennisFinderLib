import storage.interface

from typing import Union


class Player(storage.interface.Record):

    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name


class Business(object):

    def __init__(self, storage : storage.interface.Storage):
        super(Business, self).__init__()
        self.storage = storage

    def create_player(self, player : Player) -> Union[Player, None]:
        return self.storage.write(player)

    def save_player(self, player: Player) -> Union[Player, None]:
        return self.storage.update(player)