import unittest

from gamemanagerlib.storage.memory import MemoryStorage

import gamemanagerlib.business.players
import gamemanagerlib.business.teams

class Tests(unittest.TestCase):

    def test_create_team(self):

        team = gamemanagerlib.business.teams.Team(name="test")
        team_bll = gamemanagerlib.business.teams.Business(MemoryStorage())

        result = team_bll.create_team(team=team)

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, team.name)

    def test_assign_players(self):

        team = gamemanagerlib.business.teams.Team(name="test")
        teambll = gamemanagerlib.business.teams.Business(MemoryStorage())

        created_team = teambll.create_team(team=team)

        player = gamemanagerlib.business.players.Player(name="test")
        result = teambll.assign_player(team.id , player.id)

        self.assertEqual(result, True)

    def test_get_team_by_name(self):

        memory = MemoryStorage()
        memory.map["bar"] = gamemanagerlib.business.teams.Team(name="foo")

        team_bll = gamemanagerlib.business.teams.Business(memory)

        result = team_bll.get_team(name="foo")

        self.assertEqual(result, memory.map["bar"])

    def test_get_team_by_id(self):

        memory = MemoryStorage()
        memory.map[999] = gamemanagerlib.business.teams.Team(name="foo")

        team_bll = gamemanagerlib.business.teams.Business(memory)

        result = team_bll.get_team(id=999)

        self.assertEqual(result, memory.map[999])

    def test_remove_player(self):

        memory = MemoryStorage()
        team = gamemanagerlib.business.teams.Team(name="foo")
        team.player_ids.append(1)

        memory.map[999] = team

        teambll = gamemanagerlib.business.teams.Business(memory)
        teambll.remove_player(team_id=999, player_id=1)

        self.assertEqual(memory.map[999].player_ids, [])

    def test_get_team_for_player(self):

        player_id = 1

        memory = MemoryStorage()
        team = gamemanagerlib.business.teams.Team(name="foo")
        team.player_ids.append(player_id)
        memory.map[100] = team

        teambll = gamemanagerlib.business.teams.Business(memory)
        teams = teambll.get_player_teams(player_id)

        self.assertEqual(teams[0], team)