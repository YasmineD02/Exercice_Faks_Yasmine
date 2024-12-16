import unittest
from champions import find_champions

class TestFindChampions(unittest.TestCase):

    def test_empty_list(self):
        players = []
        expected = []
        self.assertEqual(set(find_champions(players)), set(expected))

    def test_single_player(self):
        players = [("A", 20, 70)]
        expected = [("A", 20, 70)]
        self.assertEqual(set(find_champions(players)), set(expected))

    def test_same_score(self):
        players = [("A", 20, 70), ("B", 25, 70), ("C", 18, 70), ("D", 21, 70)]
        expected = [("C", 18, 70)]
        self.assertEqual(set(find_champions(players)), set(expected))

    def test_same_age(self):
        players = [("A", 20, 70), ("B", 20, 75), ("C", 20, 80), ("D", 20, 85)]
        expected = [("D", 20, 85)]
        self.assertEqual(set(find_champions(players)), set(expected))

    def test_dominating_player(self):
        players = [("A", 20, 70), ("B", 18, 75)]
        expected = [("B", 18, 75)]
        self.assertEqual(set(find_champions(players)), set(expected))

    def test_no_dominance(self):
        players = [("A", 20, 70), ("B", 18, 60)]
        expected = [("A", 20, 70), ("B", 18, 60)]
        self.assertEqual(set(find_champions(players)), set(expected))

    def test_identical_players(self):
        players = [("A", 20, 70), ("B", 20, 70), ("C", 20, 70)]
        expected = [("A", 20, 70), ("B", 20, 70), ("C", 20, 70)]
        self.assertEqual(set(find_champions(players)), set(expected))

    def test_random_case_1(self):
        players = [("A", 20, 70), ("B", 18, 75), ("C", 22, 72), ("D", 25, 80)]
        expected = [("B", 18, 75), ("D", 25, 80)]
        self.assertEqual(set(find_champions(players)), set(expected))


    def test_random_case_2(self):
        players = [("A", 20, 100), ("B", 22, 80), ("C", 18, 85), ("D", 25, 90), ("E", 18, 85)]
        expected = [("A", 20, 100), ("C", 18, 85), ("E", 18, 85)]
        self.assertEqual(set(find_champions(players)), set(expected))

if __name__ == "__main__":
    unittest.main()
