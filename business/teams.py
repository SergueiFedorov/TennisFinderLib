import storage.interface


class Team(storage.interface.Record):

    def __init__(self, name):
        super(Team, self).__init__()
        self.name = name
        self.player_ids = []


class Business(object):

    def __init__(self, storage):
        self.storage = storage

    def create_team(self, team: Team) -> Team:
        return self.storage.write(team)

    def save_team(self, team: Team) -> Team:
        return self.storage.write(team)

    def assign_player(self, team_id, player_id):
        team = self.storage.read(team_id)
        team.player_ids.append(player_id)
        try:
            self.save_team(team)
            return True
        except:
            return False
