import storage.interface


class Team(storage.interface.Record):

    def __init__(self, name):
        super(Team, self).__init__()
        self.name = name


class Business(object):

    def __init__(self, storage):
        self.storage = storage

    def create_team(self, team: Team) -> Team:
        return self.storage.write(team)