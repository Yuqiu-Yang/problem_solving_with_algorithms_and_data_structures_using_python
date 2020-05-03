from ch7_breadth_first_search import *

def genLegalMoves(m, c, b):
    if b == 0:
        # if the boat is on the left side
        temp = [(max([0, m - 1])   , c  ,1), \
                (m, max([0, c - 1]),   1),\
                (max([0, m - 1]), max([0, c - 1]), 1)]
        nextStates = []
        for i in temp:
            # if state has not changed then NOT legal
            # if after the boat left, on the right bank
            # cannibals outnumbered missionaries then NOT legal
            if (m != i[0]) or (c != i[1]):
                if (i[0] == 0) or (i[1] <= i[0]):
                    nextStates.append(i)
    else:
        # if the boat is on the right side
        temp = [(min([3, m + 1])   , c  ,0),\
                (m, min([3, c + 1]),   0),\
                (min([3, m + 1]), min([3, c + 1]), 0)]
        nextStates = []
        for i in temp:
            if (m != i[0]) or (c != i[1]):
                if (i[0] == 3) or ((3-i[1]) <= (3-i[0])):
                    nextStates.append(i)
    return nextStates


def buildRiverGraph():
    g = Graph()
    for i in range(4):
        for j in range(4):
            for k in range(2):
                g.addVertex(f"{i}_{j}_{k}")
    for aVertex in g:
        m, c, b = [int(x) for x in aVertex.getId().split("_")]
        nextStates = genLegalMoves(m,c,b)
        for ns in nextStates:
            g.addEdge(f"{m}_{c}_{b}", f"{ns[0]}_{ns[1]}_{ns[2]}")
    return g


g = buildRiverGraph()

bfs(g, g.getVertex("3_3_0"))

target = "0_0_1"

pathList = traverse(g.getVertex(target))

while len(pathList) > 0:
    m, c, b = [int(x) for x in pathList.pop().split("_")]
    if b == 0:
        side = "Left"
    else:
        side = "Right"
    print(f"\tLeft side: {m} missionaries and {c} cannibals.\n\
     Right side: {3 - m} missionaries and {3 - c} cannibals.\n\
     The boat is on {side}\n")
