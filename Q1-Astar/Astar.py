from Puzzle import Puzzle
from Node import Node


def printPath(node):
    print node.getPuzzle().m_blankPosition
    while isinstance(node.m_parent, Node):
        node = node.m_parent
        if(node.getPuzzle().m_blankPosition) == (4,2):
            print "6ieme etape\n"
            print node.getPuzzle().m_puzzleState

        elif(node.getPuzzle().m_blankPosition) == (2,0):
            print "6ieme a partir de la fin \n"
            print node.getPuzzle().m_puzzleState

        else:
            print node.getPuzzle().m_blankPosition


if __name__ == '__main__':

    puzzleArray = [2, 3, 7, 4, 5, 1, -1, 11, -1, 8, 6, 10, 0, 12, 15, 9, -1, 14, -1, 20, 13, 16, 17, 18, 19]
    puzzleGoal = [1, 2, 3, 4, 5, 6, -1, 7, -1, 8, 9, 10, 0, 11, 12, 13, -1, 14, -1 ,15, 16, 17, 18, 19, 20]
    blankPosition = (2, 2)
    darkHoles = [(1, 1), (1, 3), (3, 1), (3, 3)]

    puzzle = Puzzle(puzzleArray, puzzleGoal)

    closedSet = []
    openSet = []
    startNode = Node(puzzle)
    openSet.append(Node(puzzle))
    startNode.m_open = 1

    gScore = {}
    fScore = {}
    path = {}

    startNode.m_g = 0                                               #already traveled
    startNode.m_f = startNode.m_g + startNode.getEuristic()     #estimate + already traveled

    while len(openSet) > 0:
        parentNode = min(openSet)
        if parentNode.getPuzzle().checkGoal():
            printPath(parentNode)
            break

        openSet.remove(parentNode)
        closedSet.append(parentNode)
        parentNode.m_closed = 1
        parentNode.m_open = 0

        sucessorsPuzzles = parentNode.getPuzzle().createSuccessors()
        sucessorNodes = []
        for sucessor in sucessorsPuzzles:
            sucessorNodes.append(Node(sucessor, parentNode))

        for sucessor in sucessorNodes:
            testGscore = startNode.m_g + 1
            if sucessor.m_closed == 1 and testGscore >= sucessor.m_g:
                continue

            if sucessor.m_closed == 0:

                #path[sucessor] = parentNode
                sucessor.m_g = testGscore
                sucessor.m_f = sucessor.m_g + sucessor.getEuristic()
                if sucessor.m_open == 0:
                    openSet.append(sucessor)
                    sucessor.m_open = 1

print "nombre d'etats explores : " + str(len(closedSet))