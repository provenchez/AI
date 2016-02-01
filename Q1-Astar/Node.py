from Puzzle import Puzzle


class Node:

    m_heuristic = 0
    m_puzzle = Puzzle

    def __init__(self, puzzle):
        self.m_heuristic = puzzle.h2n()
        self.m_puzzle = puzzle

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
