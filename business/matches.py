import storage.interface

from typing import Union


class Match(storage.interface.Record):

    def __init__(self, name):
        super(Match, self).__init__()
        self.name = name
        self.team_ids = []
        self.scores = []


class Business(object):

    def __init__(self, storage : storage.interface.Storage):
        self.storage = storage

    def create_match(self, match : Match) -> Union[Match, None]:
        return self.storage.write(match)

    def save_match(self, match) -> Match:

        assert match.id

        return self.storage.update(match)

    def find_match(self, id) -> Union[Match, None]:
        try:
            return self.storage.read(id)[0]
        except IndexError:
            return []

    def assign_team(self, match_id, team_id) -> bool:
        match = self.find_match(match_id)
        match.team_ids.append(team_id)
        try:
            self.save_match(match)
            return True
        except:
            # TODO: Define proper exception
            return False

    def remove_team(self, match_id, team_id) -> bool:
        match = self.find_match(id=match_id)
        try:
            match.team_ids.remove(team_id)
            self.save_match(match)
            return True
        except (IndexError, ValueError):
            return False

    def record_score(self, record) -> bool:

        assert record.id

        match = self.find_match(record.match_id)
        match.scores.append(record.id)

        try:
            self.save_match(match)
            return True
        except:
            return False
