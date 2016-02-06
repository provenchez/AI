from unittest import TestCase
from Puzzle import Puzzle

puzzleArray = [2, 3, 7, 4, 5, 1, -1, 11, -1, 8, 6, 10, 0, 12, 15, 9, -1, 14, -1, 20, 13, 16, 17, 18, 19]
puzzleGoal = [1, 2, 3, 4, 5, 6, -1, 7, -1, 8, 9, 10, 0, 11, 12, 13, -1, 14, -1, 15, 16, 17, 18, 19, 20]

class TestPuzzle(TestCase):
    puzzle = Puzzle(puzzleArray,puzzleGoal)

    def test_validateArray(self):
        self.puzzle._validateArray(puzzleArray)
        self.puzzle._validateArray(puzzleGoal)

    def test_Puzzle(self):
        blankPosition = (2, 2)
        darkHoles = [(1, 1), (1, 3), (3, 1), (3, 3)]
        goodGoal = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4),
                    6: (1, 0), 7: (1, 2), 8: (1, 4), 9: (2, 0), 10: (2, 1), 0: (2,2),
                    11: (2, 3), 12: (2, 4), 13: (3, 0), 14: (3, 2), 15: (3, 4),
                    16: (4, 0), 17: (4, 1), 18: (4, 2), 19: (4, 3), 20: (4, 4)}

        createdGoal = self.puzzle.createDictionnaryFromPuzzle(puzzleGoal)
        self.assertDictEqual(goodGoal, createdGoal)

    def test_checkGoal(self):
        goodGoal = [1, 2, 3, 4, 5, 6, -1, 7, -1, 8, 9, 10, 0, 11, 12, 13, -1, 14, -1, 15, 16, 17, 18, 19, 20]


        puzzle2 = Puzzle(goodGoal, puzzleGoal)

        self.assertTrue(puzzle2.checkGoal());

    def test_h2n(self):
        goodGoal = [1, 2, 3, 4, 5, 7, -1, 6, -1, 8, 9, 10, 0, 11, 12, 13, -1, 14, -1, 15, 16, 17, 18, 19, 20]

        puzzle2 = Puzzle(goodGoal, puzzleGoal)
        self.assertEquals(8, puzzle2.h2n())

    def test_h1n(self):
        goodGoal = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4),
                    6: (1, 0), 7: (1, 2), 8: (1, 4), 9: (2, 0), 10: (2, 1),
                    11: (2, 3), 12: (2, 4), 13: (3, 0), 14: (3, 2), 15: (3, 4),
                    16: (4, 0), 17: (4, 1), 18: (4, 2), 19: (4, 3), 20: (4, 4)}

        createdGoal = self.puzzle.createDictionnaryFromPuzzle(puzzleGoal)

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

    def test_createLeft(self):

        leftChild = self.puzzle.createLeft()
        self.assertEquals(2, abs(self.puzzle.h2n() - leftChild.h2n()))

    def test_createRigth(self):

        righthChild = self.puzzle.createRigth()
        self.assertEquals(2, abs(self.puzzle.h2n() - righthChild.h2n()))

    def test_createDown(self):

        downChid = self.puzzle.createDown()
        self.assertEquals(2, abs(self.puzzle.h2n() - downChid.h2n()))

    def test_createUp(self):
        zeroPos = self.puzzle.m_puzzleState[0]
        upChild = self.puzzle.createUp()
        zeroPosChild = upChild.m_puzzleState[0]
        self.assertEquals(1, abs(zeroPosChild[0] - zeroPos[0]))