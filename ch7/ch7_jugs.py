from ch7_breadth_first_search import *

def buildJugGraph(Jug1, Jug2):
    g = Graph()
    for i in range(Jug1 + 1):
        for j in range(Jug2 + 1):
            g.addVertex(f"{i}_{j}")
    for aVertex in g:
        v1, v2 = aVertex.getId().split("_")
        vol1 = int(v1)
        vol2 = int(v2)
        nextStates = [[vol1, 0], [0, vol2], [Jug1, vol2], \
                        [vol1, Jug2]]
        t2 = min([vol2 + vol1, Jug2])
        t1 = vol1 - (t2 - vol2)
        nextStates.append([t1,t2])
        t1 = min([vol1 + vol2, Jug1])
        t2 = vol2 - (t1 - vol1)
        nextStates.append([t1,t2])
        for ns in nextStates:
            if ns != [vol1, vol2]:
                g.addEdge(f"{v1}_{v2}", f"{ns[0]}_{ns[1]}")
    return g

g = buildJugGraph(4,3)

bfs(g, g.getVertex("0_0"))

target = 2

pathList = traverse(g.getVertex(f"{target}_{0}"))

while len(pathList) > 0:
    v_info = pathList.pop().split("_")
    print(f"Volume in Jug1 is {v_info[0]} and volume in Jug2 is {v_info[1]}")
