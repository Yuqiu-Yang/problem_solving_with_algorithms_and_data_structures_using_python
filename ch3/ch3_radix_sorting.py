from ch3_queue import Queue

def radixSort(intList):
    mainBin = Queue()
    digitBins = [Queue() for i in range(10)]

    strList, maxL = intModifier(intList)

    for i in strList:
        mainBin.enqueue(i)


    for i in range(maxL):
        for j in range(len(intList)):
            temp = mainBin.dequeue()
            ithDig = int(temp[maxL - i - 1])
            digitBins[ithDig].enqueue(temp)
        for j in range(10):
            while not digitBins[j].isEmpty():
                mainBin.enqueue(digitBins[j].dequeue())
    sortedList = []
    while not mainBin.isEmpty():
        sortedList.append(int(mainBin.dequeue()))
    return sortedList


def intModifier(intList):
    le = len(intList)
    l = []
    strList = []
    for i in intList:
        strList.append(str(i))
    for i in strList:
        l.append(len(i))
    maxL = max(l)
    for i in range(le):
        strList[i] = ("0"*(maxL - l[i])) + \
        strList[i]
    return strList, maxL
