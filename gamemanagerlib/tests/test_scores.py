import unittest

from gamemanagerlib.storage.memory import MemoryStorage

import gamemanagerlib.business.scores


class Tests(unittest.TestCase):

    def test_create_score(self):

        bll = gamemanagerlib.business.scores.Business(MemoryStorage())

        record = gamemanagerlib.business.scores.Score("team", "match", 1)

        record = bll.record_score(record)

        self.assertIsNotNone(record.id)

    def test_get_score(self):

        storage = MemoryStorage()
        storage.map["foo"] = gamemanagerlib.business.scores.Score("team", "match", 1)

        bll = gamemanagerlib.business.scores.Business(storage)

        found = bll.get_scores_for_match(team_id="team", match_id="match")

        self.assertEqual(len(found), 1)
        self.assertEqual(found[0], storage.map["foo"])