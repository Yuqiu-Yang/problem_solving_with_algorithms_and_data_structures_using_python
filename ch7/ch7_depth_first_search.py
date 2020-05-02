from ch7_graph import *

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.topologicalList = []
    def dfs(self):
        for aVertex in self:
            aVertex.setColor("white")
            aVertex.setPredecessor(-1)
        for aVertex in self:
            if aVertex.getColor() == "white":
                self.dfsvisit(aVertex)
    def dfsvisit(self, startVertex):
        startVertex.setColor("gray")
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == "white":
                nextVertex.setPredecessor(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.time)
    def getDFSTree(self, startVertex):
        treeList = []
        treeList.append(startVertex)
        succ = startVertex.getSuccessor()
        while succ:
            treeList.append(succ)
            succ = succ.getSuccessor()
        return treeList
    def topologicalSort(self):
        self.dfs()
        temp = list(self.vertList.values())
        temp.sort(key = lambda x: x.getFinish(), reverse = True)
        self.topologicalList = [x.getId() for x in temp]
        return self.topologicalList
    def SCC(self):
        self.dfs()
        self.topologicalSort()
        tempVert = [self.getVertex(x) for x in self.topologicalList]
        self.transpose()
        self.time = 0
        for aVertex in tempVert:
            aVertex.setColor("white")
            aVertex.setPredecessor(None)
        for aVertex in tempVert:
            if aVertex.getColor() == "white":
                self.dfsvisit(aVertex)
        sccDic = {}
        for aVertex in self:
            aVertex.setColor("white")
        i = 0
        for aVertex in tempVert:
            if aVertex.getColor() == "white":
                treeList = self.getDFSTree(aVertex)
                sccDic[i] = [x.getId() for x in treeList]
                for j in treeList:
                    j.setColor('black')
                i += 1
        return sccDic
