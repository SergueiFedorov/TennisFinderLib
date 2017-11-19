import unittest
import business.teams
import business.players

from storage.memory import MemoryStorage


class Tests(unittest.TestCase):

    def test_create_team(self):

        team = business.teams.Team(name="test")
        team_bll = business.teams.Business(MemoryStorage())

        result = team_bll.create_team(team=team)

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, team.name)

    def test_assign_players(self):

        team = business.teams.Team(name="test")
        teambll = business.teams.Business(MemoryStorage())

        created_team = teambll.create_team(team=team)

        player = business.players.Player(name="test")
        result = teambll.assign_player(team.id , player.id)

        self.assertEqual(result, True)

    def test_get_team_by_name(self):

        memory = MemoryStorage()
        memory.map["bar"] = business.teams.Team(name="foo")

        team_bll = business.teams.Business(memory)

        result = team_bll.get_team(name="foo")

        self.assertEqual(result, memory.map["bar"])

    def test_get_team_by_id(self):

        memory = MemoryStorage()
        memory.map["bar"] = business.teams.Team(name="foo")

        team_bll = business.teams.Business(memory)

        result = team_bll.get_team(id="bar")

        self.assertEqual(result, memory.map["bar"])

    def test_remove_player(self):

        memory = MemoryStorage()
        team = business.teams.Team(name="foo")
        team.player_ids.append(1)

        memory.map["bar"] = team

        teambll = business.teams.Business(memory)
        teambll.remove_player(team_id="bar", player_id=1)

        self.assertEqual(memory.map["bar"].player_ids, [])
