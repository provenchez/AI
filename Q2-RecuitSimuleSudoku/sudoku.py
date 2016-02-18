
import random

class Sudoku:

    m_sudokuArray =[]

    def __init__(self, array):

        self.m_sudokuArray = array

    def _validateLine(self, lineIndex):
        line = self.m_sudokuArray[lineIndex]
        return self._validateArray(line)

    def _validateColumn(self, column):
        columnArray = []
        for i in range (0,9):
            columnArray.append(self.m_sudokuArray[i][column])
        return self._validateArray(columnArray)

    def _validateArray(self, array):

        if -1 in array:
            return False
        if sum(array) != 45:
            return False

        for i in range(1, 10):
            if i not in array:
                return False

        return True

    def _validateSquare(self, squareIndex):
        lineLimits = ()
        columnLimits = ()

        if squareIndex < 3:
            lineLimits = (0,3)

        if squareIndex > 2 and squareIndex <= 5:
            lineLimits = (3,6)
            squareIndex = squareIndex - 3

        if squareIndex > 5:
            lineLimits = (6,9)
            squareIndex = squareIndex - 6

        columnLimits = (squareIndex*3, squareIndex*3+3)
        squareArray = self._getSqareFromLimits(lineLimits, columnLimits)
        return self._validateArray(squareArray)


    def _getSqareFromLimits(self, lineLimits, columnLimits):

        sqareArray = []
        for i in range (lineLimits[0], lineLimits[1]):
            for j in range (columnLimits[0], columnLimits[1]):
                sqareArray.append(self.m_sudokuArray[i][j])
        return sqareArray

    def validateSudoku(self):
        valiation = []
        for i in range(0,9):
            valiation.append(self._validateLine(i))
            valiation.append(self._validateColumn(i))
            valiation.append(self._validateSquare(i))

        if False in valiation:
            return False

        return True

    def createRandomSucessor(self):

        a = random.randint(0,8)
        b = random.randint(0,8)
        while self.m_sudokuArray[a][b] != -1:
            a = random.randint(0,8)
            b = random.randint(0,8)

        number = random.randint(1,9)

    def getValue(self):
        return 1


