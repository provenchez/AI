import math
from copy import copy

class Puzzle:

    m_puzzleState = {}
    m_puzzleGoal = {}
    m_blankPosition = ()
    m_darkHoles = []
    m_puzzleArray = []
    m_goalArray = []

    def __init__(self, puzzleArray, goalArray):

        self.m_puzzleArray = puzzleArray
        self.m_goalArray = goalArray

        self.m_puzzleState = self.createDictionnaryFromPuzzle(puzzleArray)
        self.m_puzzleGoal = self.createDictionnaryFromPuzzle(goalArray, True)

    def validateArray(self, array):

        if len(array) != 25:
            raise(InvalidArray("array length is not 25"))

    def checkGoal(self):
        return self.m_puzzleState == self.m_puzzleGoal

    def createDictionnaryFromPuzzle(self, puzzleArray, goal = False):
        puzzle = {}
        size = int(math.sqrt(len(puzzleArray)))
        for i in range (0,size):
            for j in range (0,size):
                if puzzleArray[i*size+j] == -1:
                    self.m_darkHoles.append((i,j))

                if puzzleArray[i*size+j] == 0 and not goal:
                    self.m_blankPosition = (i,j)

                if puzzleArray[i*size+j] != -1:
                    puzzle[puzzleArray[i*size+j]] = (i, j)

        return puzzle

    def h2n(self):
        sum = 0
        for i in range(0, len(self.m_puzzleState)):
            posState = self.m_puzzleState.get(i)
            posGoal = self.m_puzzleGoal.get(i)
            sum += self.calculateDarkHoles(posGoal, posState)
            sum += (abs(posState[0] - posGoal[0]) + abs(posState[1] - posGoal[1]))
        return sum

    def h1n(self):
        sum = 0
        for i in range(1, len(self.m_puzzleState)):
            if(self.m_puzzleState.get(i) != self.m_puzzleGoal.get(i)):
                sum+=1
        return sum

    def calculateDarkHoles(self, posGoal, posState):
        bonus  = 0
        if(posGoal != posState):
            if( posGoal[0]== 1 and posState[0] == 1 or posGoal[0]== 3 and posState[0] == 3) or ( posGoal[1]== 1 and posState[1] == 1 or posGoal[1]== 3 and posState[1] == 3):
                bonus = 2
        return bonus

    def createSuccessors(self):

        sucessors = []
        sucessors.append(self.createLeft())
        sucessors.append(self.createRigth())
        sucessors.append(self.createUp())
        sucessors.append(self.createDown())
        while None in sucessors:
            sucessors.remove(None)
        return sucessors

    def createLeft(self):

        if self.m_blankPosition[0] in [1, 3] or self.m_blankPosition[1] in [0]:
            return None

        leftTargetArrayPos = self.m_blankPosition[0]*5+self.m_blankPosition[1]-1
        currentBlankArrayPos = leftTargetArrayPos + 1

        leftChild = copy(self.m_puzzleArray)
        value = leftChild[leftTargetArrayPos]
        leftChild[leftTargetArrayPos] = leftChild[currentBlankArrayPos]
        leftChild[currentBlankArrayPos] = value

        return Puzzle(leftChild, self.m_goalArray)

    def createRigth(self):

        if self.m_blankPosition[0] in [1, 3] or self.m_blankPosition[1] in [4]:
            return None

        rigthTargetArrayPos = self.m_blankPosition[0]*5+self.m_blankPosition[1]+1
        currentBlankArrayPos = rigthTargetArrayPos - 1

        leftChild = copy(self.m_puzzleArray)
        value = leftChild[rigthTargetArrayPos]
        leftChild[rigthTargetArrayPos] = leftChild[currentBlankArrayPos]
        leftChild[currentBlankArrayPos] = value

        return Puzzle(leftChild, self.m_goalArray)

    def createDown(self):

        if self.m_blankPosition[0] in [4] or self.m_blankPosition[1] in [1,3]:
            return None

        DownTargetArrayPos = self.m_blankPosition[0]*5+self.m_blankPosition[1]+5
        currentBlankArrayPos = DownTargetArrayPos - 5

        leftChild = copy(self.m_puzzleArray)
        value = leftChild[DownTargetArrayPos]
        leftChild[DownTargetArrayPos] = leftChild[currentBlankArrayPos]
        leftChild[currentBlankArrayPos] = value

        return Puzzle(leftChild, self.m_goalArray)

    def createUp(self):
        if self.m_blankPosition[0] in [0] or self.m_blankPosition[1] in [1,3]:
            return None

        DownTargetArrayPos = self.m_blankPosition[0]*5+self.m_blankPosition[1]-5
        currentBlankArrayPos = DownTargetArrayPos + 5

        leftChild = copy(self.m_puzzleArray)
        value = leftChild[DownTargetArrayPos]
        leftChild[DownTargetArrayPos] = leftChild[currentBlankArrayPos]
        leftChild[currentBlankArrayPos] = value

        return Puzzle(leftChild, self.m_goalArray)



class InvalidArray(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

