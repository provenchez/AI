from unittest import TestCase
from recuit_simule import RecuitSimule

class TestRecuitSimule(TestCase):

    m_sudokuArray = [
                    [1, -1, -1,     -1, -1, -1,     -1, -1, 2],
                    [-1, -1, 8,     -1, -1, 9,       -1, 3, 7],
                    [7, -1, -1,     5, 3, -1,       -1, 8, -1],

                    [-1, 8, -1,      -1, 7, 3,       -1, 5, 4],
                    [-1, -1, 6,      4, -1, 2,      7, -1, -1],
                    [9, 7, -1,       8, 5, -1,      -1, 1, -1],

                    [-1, 1, -1,     -1, 8, 7,       -1, -1, 9],
                    [3, 4, -1,       6, -1, -1,     8, -1, -1],
                    [8, -1, -1,     -1, -1, -1,     -1, -1, 1],
                ]

    m_sudokuArrayGoal = [
                    [1, 5, 3,     7, 6, 8,     9, 4, 2],
                    [4, 6, 8,     1, 2, 9,     5, 3, 7],
                    [7, 2, 9,     5, 3, 4,     1, 8, 6],

                    [2, 8, 1,     9, 7, 3,     6, 5, 4],
                    [5, 3, 6,     4, 1, 2,     7, 9, 8],
                    [9, 7, 4,     8, 5, 6,     2, 1, 3],

                    [6, 1, 5,     3, 8, 7,     4, 2, 9],
                    [3, 4, 2,     6, 9, 1,     8, 7, 5],
                    [8, 9, 7,     2, 4, 5,     3, 6, 1],
                ]


    m_temperature = 810

    recuitSimule = RecuitSimule(m_sudokuArray, m_sudokuArrayGoal, m_temperature)

    def test_simulate(self):
        solution = self.recuitSimule.simulate()
        print solution


    def test_probability(self):
        self.recuitSimule.getProbability(400.0)

