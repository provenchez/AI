from sudoku import Sudoku


class Node:

    def __init__(self, sudoku):
        self.m_sudoku = sudoku

    def getRandomSucessor(self):
        sucessor = self.m_sudoku.createRandomSucessor()
        return Node(sucessor)

    def getValue(self):
        return self.m_sudoku.getValue()

    def show(self):
        self.m_sudoku.show()

