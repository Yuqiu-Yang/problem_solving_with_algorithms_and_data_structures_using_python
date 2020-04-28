from ch6_binary_heap import *


class priorityQueue:
    def __init__(self, variation = "min"):
        self.heap = binaryHeap(variation = variation)

    def size(self):
        return self.heap.size()
    def isEmpty(self):
        return self.heap.isEmpty()
    def enqueue(self, item):
        self.heap.insert(item)
    def dequeue(self):
        if self.size == 1:
            return self.heap.heapList.pop()
        else:
            temp = self.heap.findExtreme()
            self.heap.delExtreme()
            return temp
