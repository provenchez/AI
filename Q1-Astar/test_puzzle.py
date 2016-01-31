from unittest import TestCase
from Puzzle import Puzzle

puzzleArray = [2, 3, 7, 4, 5, 1, 11, 8, 6, 10, 12, 15, 9, 14, 20, 13, 16, 17, 18, 19]
puzzleGoal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


class TestPuzzle(TestCase):
    puzzle = Puzzle()

    def test_validateArray(self):
        self.puzzle.validateArray(puzzleArray)
        self.puzzle.validateArray(puzzleGoal)

    def test_Puzzle(self):
        blankPosition = (2, 2)
        darkHoles = [(1, 1), (1, 3), (3, 1), (3, 3)]
        goodGoal = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4),
                    6: (1, 0), 7: (1, 2), 8: (1, 4), 9: (2, 0), 10: (2, 1),
                    11: (2, 3), 12: (2, 4), 13: (3, 0), 14: (3, 2), 15: (3, 4),
                    16: (4, 0), 17: (4, 1), 18: (4, 2), 19: (4, 3), 20: (4, 4)}

        createdGoal = self.puzzle.createDictionnaryFromPuzzle(puzzleGoal, blankPosition, darkHoles)
        self.assertDictEqual(goodGoal, createdGoal)

    def test_checkGoal(self):
        blankPosition = (2, 2)
        darkHoles = [(1, 1), (1, 3), (3, 1), (3, 3)]
        goodGoal = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4),
                    6: (1, 0), 7: (1, 2), 8: (1, 4), 9: (2, 0), 10: (2, 1),
                    11: (2, 3), 12: (2, 4), 13: (3, 0), 14: (3, 2), 15: (3, 4),
                    16: (4, 0), 17: (4, 1), 18: (4, 2), 19: (4, 3), 20: (4, 4)}

        createdGoal = self.puzzle.createDictionnaryFromPuzzle(puzzleGoal, blankPosition, darkHoles)
        self.assertTrue(self.puzzle.checkGoal(goodGoal, goodGoal));

    def test_h2n(self):
        blankPosition = (2, 2)
        darkHoles = [(1, 1), (1, 3), (3, 1), (3, 3)]
        goodGoal = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4),
                    7: (1, 0), 6: (1, 2), 8: (1, 4), 9: (2, 0), 10: (2, 1),
                    11: (2, 3), 12: (2, 4), 13: (3, 0), 14: (3, 2), 15: (3, 4),
                    16: (4, 0), 17: (4, 1), 18: (4, 2), 19: (4, 3), 20: (4, 4)}
        createdGoal = self.puzzle.createDictionnaryFromPuzzle(puzzleGoal, blankPosition, darkHoles)

        self.assertEquals(8, self.puzzle.h2n(goodGoal, createdGoal))

    def test_h1n(self):
        blankPosition = (2, 2)
        darkHoles = [(1, 1), (1, 3), (3, 1), (3, 3)]
        goodGoal = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4),
                    6: (1, 0), 7: (1, 2), 8: (1, 4), 9: (2, 0), 10: (2, 1),
                    11: (2, 3), 12: (2, 4), 13: (3, 0), 14: (3, 2), 15: (3, 4),
                    16: (4, 0), 17: (4, 1), 18: (4, 2), 19: (4, 3), 20: (4, 4)}

        createdGoal = self.puzzle.createDictionnaryFromPuzzle(puzzleGoal, blankPosition, darkHoles)

        self.assertEquals(0, self.puzzle.h1n(createdGoal, goodGoal))


    def test_calculateDarkHoles(self):
        pos1 = (0,1)
        pos2 = (2,1)
        bonus = self.puzzle.calculateDarkHoles(pos1,pos2)
        self.assertEquals(bonus,2);

    def test_calculateDarkHoles2(self):
        pos1 = (0,2)
        pos2 = (2,1)
        bonus = self.puzzle.calculateDarkHoles(pos1,pos2)
        self.assertEquals(bonus,0);

    def test_calculateDarkHoles3(self):
        pos1 = (1,2)
        pos2 = (1,4)
        bonus = self.puzzle.calculateDarkHoles(pos1,pos2)
        self.assertEquals(bonus,2);

    def test_calculateDarkHoles3(self):
        pos1 = (3,2)
        pos2 = (3,0)
        bonus = self.puzzle.calculateDarkHoles(pos1,pos2)
        self.assertEquals(bonus,2);

    def test_calculateDarkHoles4(self):
        pos1 = (4,0)
        pos2 = (2,4)
        bonus = self.puzzle.calculateDarkHoles(pos1,pos2)
        self.assertEquals(bonus,0);
