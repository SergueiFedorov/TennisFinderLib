import storage.interface


class Game(storage.interface.Record):

    def __init__(self, name):
        super(Game, self).__init__()
        self.name = name
        self.team_ids = []


class Business(object):

    def __init__(self, storage : storage.interface.Storage):
        self.storage = storage

    def create_game(self, game : Game) -> Game:
        return self.storage.write(game)

    def save_game(self, game) -> Game:
        return self.storage.update(game)

    def find_game(self, id) -> Game:
        return self.storage.read(id)

    def assign_team(self, game_id, team_id) -> Game:
        game = self.find_game(game_id)
        game.team_ids.append(team_id)
        try:
            self.save_game(game)
            return True
        except:
            # TODO: Define proper exception
            return False