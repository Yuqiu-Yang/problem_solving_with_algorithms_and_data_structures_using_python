from ch7_graph import *
import sys
from ch6_pq_pythonds import *

def prim(G, start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPredecessor(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getDistance() + \
                        currentVert.getWeight(nextVert)
            if newCost < nextVert.setDistance() and nextVert in pq:
                nextVert.setPredecessor(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)
