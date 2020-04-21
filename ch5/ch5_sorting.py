# All the functions here will sort the list into an ascending order

def bubbleSort(aList):
    for passnum in range(len(aList) - 1, 0, -1):
        for i in range(passnum):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]

def shortBubbleSort(aList):
    exchange = True
    passnum = len(aList) - 1
    while (passnum > 0) and exchange:
        exchange = False
        for i in range(passnum):
            if aList[i] > aList[i + 1]:
                exchange = True
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
        passnum -= 1


def selectionSort(aList):
    for passnum in range(len(aList), 0, -1):
        max_pos = 0
        for i in range(1,passnum):
            if aList[i] > aList[max_pos]:
                max_pos = i
        aList[i], aList[max_pos] = aList[max_pos], aList[i]

def insertionSort(aList):
    for i in range(1, len(aList)):
        currentValue = aList[i]
        position = i - 1
        while (aList[position] > currentValue) and (position >= 0):
            aList[position + 1] = aList[position]
            position -= 1
        aList[position + 1] = currentValue


def shellSort(aList):
    pass


def mergeSort(aList):
    pass

def quickSort(aList):
    pass
