class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.distance = 0
        self.predecessor = None
    def getColor(self):
        return self.color
    def getDistance(self):
        return self.distance
    def getPredecessor(self):
        return self.predecessor
    def setColor(self, co):
        self.color = co
    def setDistance(self, d):
        self.distance = d
    def setPredecessor(self, pred):
        self.predecessor = pred 
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo: ' \
                + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self, n):
        return n in self.vertList
    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())
