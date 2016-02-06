class Sudoku:

    m_sudokuArray =[]

    def __init__(self, array):

        self.m_sudokuArray = array

    def validateLine(self, lineIndex):
        line = self.m_sudokuArray[lineIndex]
        return self._validateArray(line)

    def validateColumn(self, column):
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

    def validateSquare(self,squareIndex):
        lineLimits = ()
        columnLimits = ()

        if squareIndex < 3:
            lineLimits = (0,3)

        if squareIndex > 2 and squareIndex <= 5:
            lineLimits = (3,5)
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


