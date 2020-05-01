from ch7_graph import *
from ch3_queue import *

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
    x = y
    while x.getPredecessor():
        print(x.getId())
        x = x.getPredecessor()
    print(x.getId())
