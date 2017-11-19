import storage.interface


class Score(storage.interface.Record):

    def __init__(self, team_id, match_id, value):
        super(Score, self).__init__()

        self.team_id = team_id
        self.match_id = match_id
        self.value = value


class Business(storage.interface.Storage):

    def __init__(self, storage):
        self.storage = storage

    def record_score(self, record : Score) -> Score:
        return self.storage.write(record)

    def get_store(self, id):
        return self.storage.read(id)

    def get_scores_for_match(self, match_id, team_id):
        return self.storage.read(where={"match_id": match_id, "team_id": team_id})