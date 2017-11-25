from typing import Union

import gamemanagerlib.storage.interface


class Team(gamemanagerlib.storage.interface.Record):

    def __init__(self, name):
        super(Team, self).__init__()
        self.name = name
        self.player_ids = []


class Business(object):

    def __init__(self, storage):
        self.storage = storage

    def create_team(self, team: Team) -> Union[Team, None]:
        return self.storage.write(team)

    def save_team(self, team: Team) -> Team:
        return self.storage.write(team)

    def get_team(self, id=None, name=None) -> Union[Team, None]:
        try:
            return self.storage.read(id, where={"name": name})[0]
        except IndexError:
            return None

    def remove_player(self, team_id, player_id) -> bool:
        team = self.get_team(id=team_id)
        try:
            team.player_ids.remove(player_id)
            self.save_team(team)
            return True
        except (ValueError, IndexError):
            return False

    def assign_player(self, team_id, player_id) -> bool:
        team = self.get_team(team_id)
        try:
            team.player_ids.append(player_id)
            self.save_team(team)
            return True
        except (AttributeError,):
            return False

    def get_player_teams(self, player_id) -> list:
        return self.storage.read(contains={"player_ids": player_id})