from unittest import TestCase
from sudoku import Sudoku
import math


class TestSudoku(TestCase):
    sudokuArray = [
        [1, -1, -1, -1, -1, -1, -1, -1, 2],
        [-1, -1, 8, -1, -1, 9, -1, 3, 7],
        [7, -1, -1, 5, 3, -1, -1, 8, -1],

        [-1, 8, -1, -1, 7, 3, -1, 5, 4],
        [-1, -1, 6, 4, -1, 2, 7, -1, -1],
        [9, 7, -1, 8, 5, -1, -1, 1, -1],

        [-1, 1, -1, -1, 8, 7, -1, -1, 9],
        [3, 4, -1, 6, -1, -1, 8, -1, -1],
        [8, -1, -1, -1, -1, -1, -1, -1, 1],
    ]

    sudokuArrayGoal = [
        [1, 5, 3, 7, 6, 8, 9, 4, 2],
        [4, 6, 8, 1, 2, 9, 5, 3, 7],
        [7, 2, 9, 5, 3, 4, 1, 8, 6],

        [2, 8, 1, 9, 7, 3, 6, 5, 4],
        [5, 3, 6, 4, 1, 2, 7, 9, 8],
        [9, 7, 4, 8, 5, 6, 2, 1, 3],

        [6, 1, 5, 3, 8, 7, 4, 2, 9],
        [3, 4, 2, 6, 9, 1, 8, 7, 5],
        [8, 9, 7, 2, 4, 5, 3, 6, 1],
    ]

    m_sudoku = Sudoku(sudokuArrayGoal)

    def test_validateLine(self):
        validLine = False
        for i in range(0, 9):
            validLine = self.m_sudoku._validateLine(i)
            if not validLine:
                self.fail()
        self.assertTrue(validLine)

    def test_validateColumn(self):
        validColumn = False
        for i in range(0, 9):
            validColumn = self.m_sudoku._validateColumn(i)
            if not validColumn:
                self.fail()
        self.assertTrue(validColumn)

    def testValidateSquare(self):
        validSquare = False
        for i in range(0, 9):
            validSquare = self.m_sudoku._validateSquare(i)
            if not validSquare:
                self.fail()
        self.assertTrue(validSquare)

    def testValidateSudoku(self):
        self.assertTrue(self.m_sudoku.validateSudoku())

    def testValidateSudokuBad(self):
        self.assertFalse(Sudoku(self.sudokuArray).validateSudoku())


    def test_show(self):
        self.m_sudoku.show()
