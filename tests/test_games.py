import unittest
import business.matches
import business.teams
import business.scores
from storage.memory import MemoryStorage


class Tests(unittest.TestCase):

    def test_create_match(self):

        bll = business.matches.Business(storage=MemoryStorage())
        match = bll.create_match(business.matches.Match(name="MyMatch"))

        self.assertIsNotNone(match.id)

        retrieved_match = bll.find_match(match.id)

        self.assertEqual(retrieved_match.name, match.name)

    def test_assign_team(self):
        matchbll = business.matches.Business(storage=MemoryStorage())
        teambll = business.teams.Business(storage=MemoryStorage())

        match = matchbll.create_match(business.matches.Match(name="MyMatch"))
        team = teambll.create_team(business.teams.Team(name="MyTeam"))

        result = matchbll.assign_team(match.id, team.id)

        self.assertEqual(result, True)

    def test_record_score(self):
        matchbll = business.matches.Business(storage=MemoryStorage())
        match = matchbll.create_match(business.matches.Match("foo"))

        score = business.scores.Score("test", match.id, 1)
        score.id = 1

        result = matchbll.record_score(score)

        self.assertEqual(result, True)
        self.assertEqual(matchbll.find_match(match.id), match)




