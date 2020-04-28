from ch6_binary_heap import *

def binaryHeapSort(aList):
    sortedList = []
    t = binaryHeap()
    t.buildHeap(aList)
    for i in range(len(aList) - 1):
        sortedList.append(t.findExtreme())
        t.delExtreme()
    sortedList.append(t.findExtreme())
    return sortedList
