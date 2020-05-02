from ch7_graph import *

class Queue(object):
    def __init__(self):
        self.item = []
        self.queue_size = 0
    def isEmpty(self):
        return self.queue_size == 0
    def enqueue(self, item):
        self.item.insert(0, item)
        self.queue_size += 1
    def dequeue(self):
        self.queue_size -= 1
        return self.item.pop()
    def size(self):
        return self.queue_size

def bfs(g, start):
    start.setDistance(0)
    start.setPredecessor(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPredecessor(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor("black")

def traverse(y):
    path = []
    x = y
    while x.getPredecessor():
        path.append(x.getId())
        x = x.getPredecessor()
    path.append(x.getId())
    return path



def allPairsShortestPath(g):
    pathDict = {}
    for v in g:
        pathDict[v.getId()] = {}
        g.resetGraph()
        bfs(g, v)
        for w in g:
            if v != w:
                pathList = traverse(w)
                if pathList[-1] != v.getId():
                    pathList = None
                pathDict[v.getId()][w.getId()] = pathList

    return pathDict
