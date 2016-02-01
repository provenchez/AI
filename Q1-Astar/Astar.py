from Puzzle import Puzzle
from Node import Node

if __name__ == '__main__':

    puzzleArray = [2, 3, 7, 4, 5, 1, -1, 11, -1, 8, 6, 10, 0, 12, 15, 9, -1, 14, -1, 20, 13, 16, 17, 18, 19]
    puzzleGoal = [1, 2, 3, 4, 5, 6, -1, 7, -1, 8, 9, 10, 0, 11, 12, 13, -1, 14, -1 ,15, 16, 17, 18, 19, 20]
    blankPosition = (2, 2)
    darkHoles = [(1, 1), (1, 3), (3, 1), (3, 3)]

    puzzle = Puzzle(puzzleArray, puzzleGoal,blankPosition, darkHoles)

    closedSet = []
    openSet = []

    openSet.append(Node(puzzle))

    while len(openSet) > 0:
        currentNode = min(openSet)
        closedSet.append(currentNode)
        openSet.remove(currentNode)

        if currentNode.getPuzzle().checkGoal():
            break #traceback

        sucessorsPuzzles = currentNode.getPuzzle().createSuccessors()


        print "test"



