from Puzzle import Puzzle


class Node:

    m_heuristic = 0
    m_puzzle = Puzzle
    m_parent = 0
    m_g = 0
    m_f = 0

    def __init__(self, puzzle, parent = None):
        self.m_heuristic = puzzle.h2n()
        self.m_puzzle = puzzle
        self.m_parent = parent

    def __cmp__(self, other):
        if self.m_heuristic < other.m_heuristic:
            return -1
        elif self.m_heuristic == other.m_heuristic:
            return 0
        else:
            return 1


    def getEuristic(self):
        return self.m_heuristic


    def getPuzzle(self):
        return self.m_puzzle

    def setParent(self, node):
        self.m_parent = node

    def getParent(self):
        return self.m_parent
