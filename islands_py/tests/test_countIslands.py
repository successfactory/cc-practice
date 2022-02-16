import countIslands
import unittest


class CountIslandsTest(unittest.TestCase):
    def test_countIslands_KnownBoard(self):
        M = [[1, 1, 0, 0, 1, 0],
             [0, 1, 0, 0, 0, 1],
             [1, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1],
             [1, 1, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 0]]
        c = countIslands.CIslandCounter(M)
        self.assertEqual(6, c.getIslands())

    def test_countIslands_OpenSea(self):
        M = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
        c = countIslands.CIslandCounter(M)
        self.assertEqual(0, c.getIslands())

    def test_countIslands_Checkers(self):
        M = [[1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1]]
        c = countIslands.CIslandCounter(M)
        self.assertEqual(1, c.getIslands())

    def test_countIslands_MainLand(self):
        M = [[1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1]]
        c = countIslands.CIslandCounter(M)
        self.assertEqual(1, c.getIslands())

    def test_countIslands_Lake(self):
        M = [[1, 1, 1, 1, 1, 1],
             [1, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 1],
             [1, 1, 0, 0, 1, 1],
             [1, 1, 1, 1, 1, 1]]
        c = countIslands.CIslandCounter(M)
        self.assertEqual(1, c.getIslands())

    def test_countIslands_LakeIsland(self):
        M = [[1, 1, 1, 1, 1, 1],
             [1, 1, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 1],
             [1, 0, 0, 2, 0, 1],
             [1, 1, 0, 0, 1, 1],
             [1, 1, 1, 1, 1, 1]]
        c = countIslands.CIslandCounter(M)
        self.assertEqual(2, c.getIslands())
