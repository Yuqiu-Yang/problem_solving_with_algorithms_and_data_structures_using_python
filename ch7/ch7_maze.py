from ch4_maze import Maze
from ch7_breadth_first_search import *
PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'
def mazeBuildGraph(maze):
    g = Graph()
    for i in range(maze.rowsInMaze):
        for j in range(maze.columnsInMaze):
            if maze.mazelist[i][j] in [" ",'S']:
                g.addVertex(f"{i}_{j}")
    for i in range(maze.rowsInMaze):
        for j in range(maze.columnsInMaze):
            if maze.mazelist[i][j] in [" ",'S']:
                surrendCord = [(max([0, i - 1]), j), \
                                (min([maze.rowsInMaze - 1, i + 1]),  j),\
                                (i, max([0, j - 1])),
                                (i, min([maze.columnsInMaze - 1, j + 1]))]
                for c in surrendCord:
                    if (c != (i, j)) and (maze.mazelist[c[0]][c[1]] in [" ",'S']):
                        g.addEdge(f"{i}_{j}", f"{c[0]}_{c[1]}")
                        g.addEdge(f"{c[0]}_{c[1]}", f"{i}_{j}")

    return g

def bfsMaze(mazeFile = 'ch4_maze2.txt'):
    myMaze = Maze(mazeFile)
    myMaze.drawMaze()
    g = mazeBuildGraph(myMaze)
    start = g.getVertex(f"{myMaze.startRow}_{myMaze.startCol}")
    myMaze.updatePosition(myMaze.startRow, myMaze.startCol, PART_OF_PATH)
    bfs(g, start)
    exitVert = [x for x in g if (int(x.getId().split("_")[0]) == 0)\
                            or (int(x.getId().split("_")[0]) == myMaze.rowsInMaze-1) \
                            or (int(x.getId().split("_")[1]) == 0)\
                            or (int(x.getId().split("_")[1]) == myMaze.columnsInMaze-1)][0]
    pathList = traverse(exitVert)
    if pathList[-1] != start.getId():
        print("Can not be solved")
    else:
        pathList.pop()
        pathMaze = [x.split('_') for x in pathList]
        while len(pathMaze) > 0:
            pos = pathMaze.pop()
            myMaze.updatePosition(int(pos[0]),int(pos[1]) , PART_OF_PATH)

bfsMaze()
