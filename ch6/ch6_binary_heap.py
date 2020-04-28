import operator
class binaryHeap:
    def __init__(self, variation = "min", limit_size = -1):
        self.heapList = [0]
        self.size = 0
        self.variation = variation
        self.limitSize = limit_size
    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.percolateUp(self.size)
        if self.limitSize >= 0:
            while self.size > self.limitSize:
                self.delExtreme()
    def percolateUp(self, i):
        oper = {"min": operator.lt,
                "max": operator.gt}
        while i // 2 != 0:
            if oper[self.variation](self.heapList[i], self.heapList[i//2]):
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i //=2
    def findExtreme(self):
        return self.heapList[1]
    def delExtreme(self):
        self.heapList[1] = self.heapList.pop()
        self.size -= 1
        self.percolateDown(1)
    def percolateDown(self, i):
        oper = {"min": operator.gt,
                "max": operator.lt}
        while (2 * i) <= self.size:
            eC = self.extremeChild(i)
            if oper[self.variation](self.heapList[i], self.heapList[eC]):
                self.heapList[i], self.heapList[eC] = self.heapList[eC], self.heapList[i]
            i = eC
    def extremeChild(self, i):
        oper = {"min": operator.lt,
                "max": operator.gt}
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if oper[self.variation](self.heapList[2 * i], self.heapList[2 * i + 1]):
                return 2 * i
            else:
                return 2 * i + 1
    def isEmpty(self):
        return self.size == 0
    def length(self):
        return self.size
    def buildHeap(self, heap_list):
        self.size = len(heap_list)
        self.heapList = [0] + heap_list
        i = self.size // 2
        while(i > 0):
            self.percolateDown(i)
            i -= 1
        if self.limitSize >= 0:
            while self.size > self.limitSize:
                self.delExtreme()
