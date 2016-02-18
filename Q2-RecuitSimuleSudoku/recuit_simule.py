from Node import Node
from sudoku import Sudoku
import random
import math

class RecuitSimule():

    m_sudokuSchedule = []
    m_sudokuProblem = []
    m_temperature = []

    def __init__(self, sudokuProblem, sudokuSchedule, temperature):
        self.m_sudokuProblem = sudokuProblem
        self.m_sudokuSchedule = sudokuSchedule
        self.m_temperature = temperature

    def simulate(self):

        currentNode = Node(Sudoku(self.m_sudokuProblem))
        found = False

        while not found:
            self.m_temperature = self.scheduleTemp()

            if self.m_temperature == 0:
                found = True

            nextNode = currentNode.getRandomSucessor()

            deltaE = nextNode.getValue() - currentNode.getValue()

            probability = self.getProbability(deltaE)
            if random.random() < probability:
                currentNode = nextNode


        return currentNode

    def getProbability(self, deltaE):
        probability = math.e**(deltaE/self.m_temperature)
        return probability



    def scheduleTemp(self):
        return self.m_temperature - 0.1