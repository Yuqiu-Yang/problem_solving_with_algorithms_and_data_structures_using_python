from ch7_graph import *

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = getLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1,-2), (-1,2),(-2,-1),(-2,1),\
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and \
                legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

def posToNodeId(x, y, bdSize):
    return x + bdSize * y


def orderedByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor() == "white":
                    c += 1
            resList.append((c,v))
    resList.sort(key = lambda x: x[0])
    return [y[1] for y in resList]

def knightTour(n, path, u, limit):
    u.setColor("gray")
    path.append(u)
    if u < limit:
        nbrList = orderedByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white":
                done = knightTour(n + 1, path, nbrList[i], limit)
            i += 1
        if not done:
            path.pop()
            u.setColor("white")
    else:
        done = True
    return done
