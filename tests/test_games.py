import unittest
import business.matches
import business.teams
from storage.memory import MemoryStorage


class Tests(unittest.TestCase):

    def test_create_game(self):

        bll = business.matches.Business(storage=MemoryStorage())
        game = bll.create_game(business.matches.Game(name="MyGame"))

        self.assertIsNotNone(game.id)

        retrieved_game = bll.find_game(game.id)

        self.assertEqual(retrieved_game.name, game.name)

    def test_assign_team(self):

        gamebll = business.matches.Business(storage=MemoryStorage())
        teambll = business.teams.Business(storage=MemoryStorage())

        game = gamebll.create_game(business.matches.Game(name="MyGame"))
        team = teambll.create_team(business.teams.Team(name="MyTeam"))

        result = gamebll.assign_team(game.id, team.id)

        self.assertEqual(result, True)


