import copy
import random


class Sudoku:
    m_sudokuArray = []
    m_fixedNodes = []

    def __init__(self, array, fixedNodes):

        self.m_fixedNodes = fixedNodes
        self.m_sudokuArray = array

    def _validateLine(self, lineIndex, partial=False):
        line = self.m_sudokuArray[lineIndex]
        return self._validateArray(line, partial)

    def _validateColumn(self, column, partial=False):
        columnArray = []
        for i in range(0, 9):
            columnArray.append(self.m_sudokuArray[i][column])
        return self._validateArray(columnArray, partial)

    def _validateArray(self, array, partial=False):

        if not partial:
            if -1 in array:
                return False
            if sum(array) != 45:
                return False

            for i in range(1, 10):
                if i not in array:
                    return False

            return True

        if partial:
            for i in range(1, 10):
                if array.count(i) > 1:
                    return False
            return True

    def _validateSquare(self, squareIndex, partial=False):
        lineLimits = ()
        columnLimits = ()

        if squareIndex < 3:
            lineLimits = (0, 3)

        if squareIndex > 2 and squareIndex <= 5:
            lineLimits = (3, 6)
            squareIndex = squareIndex - 3

        if squareIndex > 5:
            lineLimits = (6, 9)
            squareIndex = squareIndex - 6

        columnLimits = (squareIndex * 3, squareIndex * 3 + 3)
        squareArray = self._getSqareFromLimits(lineLimits, columnLimits)
        return self._validateArray(squareArray, partial)

    def _getSqareFromLimits(self, lineLimits, columnLimits):

        sqareArray = []
        for i in range(lineLimits[0], lineLimits[1]):
            for j in range(columnLimits[0], columnLimits[1]):
                sqareArray.append(self.m_sudokuArray[i][j])
        return sqareArray

    def validateSudoku(self):
        valiation = []
        for i in range(0, 9):
            valiation.append(self._validateLine(i))
            valiation.append(self._validateColumn(i))
            valiation.append(self._validateSquare(i))

        if False in valiation:
            return False

        return True

    def createRandomSucessor(self):

        a = random.randint(0, 8)
        b = random.randint(0, 8)
        while (a, b) in self.m_fixedNodes:
            a = random.randint(0, 8)
            b = random.randint(0, 8)

        sqareOne = self._getSquareIndex(a,b)

        c = random.randint(0, 8)
        d = random.randint(0, 8)
        sqareTwo = self._getSquareIndex(c,d)
        while (c, d) in self.m_fixedNodes or (a, b) == (c, d) or sqareOne != sqareTwo:
            c = random.randint(0, 8)
            d = random.randint(0, 8)
            sqareTwo = self._getSquareIndex(c,d)

        self.m_sudokuArray[a][b], self.m_sudokuArray[c][d] = self.m_sudokuArray[c][d], self.m_sudokuArray[a][b]
        newSudoku = Sudoku(copy.deepcopy(self.m_sudokuArray), self.m_fixedNodes)
        self.m_sudokuArray[c][d], self.m_sudokuArray[a][b] = self.m_sudokuArray[a][b], self.m_sudokuArray[c][d]
        return newSudoku

    def getValue(self):
        # nombre d'erreurs
        numberOferrors = 0
        for i in range(0, 9):  # pour chaque chiffre
            for j in range(0, 9):  # pour chaque ligne
                if self.m_sudokuArray[j].count(i) > 1:
                    numberOferrors += 1

                colonne = []
                for k in range(0, 9):
                    colonne.append(self.m_sudokuArray[k][j])
                if colonne.count(j) > 1:
                    numberOferrors += 1


        return numberOferrors

    def _validateUncompleteAdditionOfNumber(self, lineIndex, columnIndex):

        if self._validateLine(lineIndex, True) and self._validateColumn(columnIndex, True):

            lineMultiplier = 0
            if lineIndex >= 3:
                lineMultiplier += 1
            if lineIndex >= 6:
                lineMultiplier += 1

            columnMultiplier = 0
            if columnIndex >= 3:
                columnMultiplier += 1
            if columnIndex >= 6:
                columnMultiplier += 1

            squareIndex = lineMultiplier * 3 + columnMultiplier

            if self._validateSquare(squareIndex, True):
                return True
        return False

    def show(self):
        outputString = ""
        for i in range(0, 9):
            if i == 3 or i == 6:
                outputString += "----------------------------------\n"
            for j in range(0, 9):
                if j == 2 or j == 5:
                    outputString += str(self.m_sudokuArray[i][j]) + " | "
                else:
                    outputString += str(self.m_sudokuArray[i][j]) + "   "

            outputString += "\n"
        print outputString

    def setFixedNodes(self, fixedNodes):
        self.m_fixedNodes = fixedNodes

    def getFixedNodes(self):
        return self.m_fixedNodes

    def populate(self):
        for i in range(0,9):
            self._populateSquare(i)

    def _populateSquare(self, squareIndex):
        lineLimits = ()
        columnLimits = ()

        if squareIndex < 3:
            lineLimits = (0, 3)

        if squareIndex > 2 and squareIndex <= 5:
            lineLimits = (3, 6)

        if squareIndex > 5:
            lineLimits = (6, 9)

        if squareIndex == 0 or squareIndex == 3 or squareIndex == 6:
            columnLimits = (0,3)

        if squareIndex == 1 or squareIndex == 4 or squareIndex == 7:
            columnLimits = (3,6)

        if squareIndex == 2 or squareIndex == 5 or squareIndex == 8:
            columnLimits = (6,9)

        alreadyThereArray = []
        for i in range(lineLimits[0],lineLimits[1]):
            for j in range(columnLimits[0], columnLimits[1]):
                if (i,j) in self.m_fixedNodes:
                    alreadyThereArray.append(self.m_sudokuArray[i][j])
                else:
                    for k in range(1,10):
                        if k not in alreadyThereArray:
                            self.m_sudokuArray[i][j] = k
                            alreadyThereArray.append(k)
                            break




    def _getSquareIndex(self, lineIndex, columnIndex):
        lineMultiplier = 0
        if lineIndex >= 3:
            lineMultiplier += 1
        if lineIndex >= 6:
            lineMultiplier += 1

        columnMultiplier = 0
        if columnIndex >= 3:
            columnMultiplier += 1
        if columnIndex >= 6:
            columnMultiplier += 1

        return lineMultiplier * 3 + columnMultiplier
