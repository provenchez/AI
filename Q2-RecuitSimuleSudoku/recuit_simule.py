from Node import Node
from sudoku import Sudoku
import random
import math

class RecuitSimule():

    m_sudokuSchedule = []
    m_sudokuProblem = []
    m_temperature = []

    def __init__(self, sudokuProblem, fixedNodes, temperature):
        self.m_sudokuProblem = sudokuProblem
        self.m_fixedNodes = fixedNodes
        self.m_temperature = temperature

    def simulate(self):

        currentNode = Node(Sudoku(self.m_sudokuProblem, self.m_fixedNodes))
        currentNode.m_sudoku.populate()
        found = False

        while not found:
            self.m_temperature = self.scheduleTemp()

            if currentNode.getValue() <= 0 and currentNode.m_sudoku.validateSudoku():
                found = True
                return currentNode

            if self.m_temperature < 0.00027:
                currentNode = self.reheat()
                print "REHEAT"

            nextNode = currentNode.getRandomSucessor()

            deltaE = currentNode.getValue() - nextNode.getValue()
            print nextNode.getValue()

            probability = self.getProbability(deltaE)
            if random.random() < probability:
                currentNode = nextNode


    def getProbability(self, deltaE):
        probability = math.e**(deltaE/self.m_temperature)
        return probability



    def scheduleTemp(self):
        return self.m_temperature * 0.999

    def reheat(self):
        self.m_temperature = 810
        return Node(Sudoku(self.m_sudokuProblem, self.m_fixedNodes))