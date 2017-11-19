import unittest
import business.scores
from storage.memory import MemoryStorage


class Tests(unittest.TestCase):

    def test_create_score(self):

        bll = business.scores.Business(MemoryStorage())

        record = business.scores.Score("team", "game", 1)

        record = bll.record_score(record)

        self.assertIsNotNone(record.id)

    def test_get_score(self):

        storage = MemoryStorage()
        storage.map["foo"] = business.scores.Score("team", "game", 1)

        bll = business.scores.Business(storage)

        found = bll.get_scores_for_game(team_id="team", game_id="game")

        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], storage.map["foo"])