import unittest

from gamemanagerlib.storage.memory import MemoryStorage

import gamemanagerlib.business.scores
import gamemanagerlib.business.matches
import gamemanagerlib.business.teams

class Tests(unittest.TestCase):

    def test_create_match(self):

        bll = gamemanagerlib.business.matches.Business(storage=MemoryStorage())
        match = bll.create_match(gamemanagerlib.business.matches.Match(name="MyMatch"))

        self.assertIsNotNone(match.id)

        retrieved_match = bll.find_match(match.id)

        self.assertEqual(retrieved_match.name, match.name)

    def test_assign_team(self):
        match_bll = gamemanagerlib.business.matches.Business(storage=MemoryStorage())
        team_bll = gamemanagerlib.business.teams.Business(storage=MemoryStorage())

        match = match_bll.create_match(gamemanagerlib.business.matches.Match(name="MyMatch"))
        team = team_bll.create_team(gamemanagerlib.business.teams.Team(name="MyTeam"))

        result = match_bll.assign_team(match.id, team.id)

        self.assertEqual(result, True)

    def test_record_score(self):
        matchbll = gamemanagerlib.business.matches.Business(storage=MemoryStorage())
        match = matchbll.create_match(gamemanagerlib.business.matches.Match("foo"))

        score = gamemanagerlib.business.scores.Score("test", match.id, 1)
        score.id = 1

        result = matchbll.record_score(score)

        self.assertEqual(result, True)
        self.assertEqual(matchbll.find_match(match.id), match)




