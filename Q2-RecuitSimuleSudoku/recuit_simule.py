from Node import Node

class RecuitSimule():

    m_sudokuSchedule = []
    m_sudokuProblem = []
    m_temperature = []

    def __init__(self, sudokuProblem, sudokuSchedule, temperature):
        self.m_sudokuProblem = sudokuProblem
        self.m_sudokuSchedule = sudokuSchedule
        self.m_temperature = temperature

    def simulate(self):

        currentNode = Node(self.m_sudokuProblem)
        found = True

        while not found:
            self.m_temperature = self.scheduleTemp()

            if self.m_temperature == 0:
                return currentNode

            nextNode = currentNode.getSucessor()

            if (nextNode.getValue() - currentNode.getValue()) > 0:
                currentNode = nextNode



    def scheduleTemp(self):
        return 1