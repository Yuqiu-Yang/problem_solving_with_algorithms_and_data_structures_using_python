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

def bidirectionalBubbleSort(aList):
    exchange = True
    endPt = len(aList) - 1
    startPt = 0
    while exchange and (endPt > startPt):
        exchange = False
        for i in range(startPt, endPt):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
        endPt -= 1
        for i in range(endPt, startPt, -1):
            if aList[i] < aList[i - 1]:
                exchange = True
                aList[i], aList[i - 1] = aList[i - 1], aList[i]
        startPt += 1



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


def shellSort(aList, gap = "Half"):
    if gap == "Half":
        sublistCount = len(aList)//2
        while sublistCount > 0:
            for startposition in range(sublistCount):
                gapInsertionSort(aList, startposition, sublistCount)
            sublistCount //=2
    else:
        for i in range(gap):
            gapInsertionSort(aList, i, gap)
        insertionSort(aList)


def gapInsertionSort(aList, start, gap):
    for i in range(start + gap, len(aList), gap):
        currentValue = aList[i]
        position = i - gap
        while (aList[position] > currentValue) and (position >= start):
            aList[position + gap] = aList[position]
            position -= gap
        aList[position + gap] = currentValue


def mergeSort(aList, start, end):
    if end > start:
        midPt = (start + end + 1)//2
        mergeSort(aList, start, midPt - 1)
        mergeSort(aList, midPt, end)
        i = 0
        j = 0
        l_count = 0
        r_count = 0
        while (l_count <= (midPt - 1 - start)) and (r_count <= (end - midPt)):
            if aList[start + i] > aList[midPt + j]:
                temp = aList[midPt + j]
                for l in range(midPt + j - 1, start + i - 1, -1):
                    aList[l + 1] = aList[l]
                aList[start + i] = temp
                r_count += 1
                i += 1
                j += 1
            else:
                l_count += 1
                i += 1

def mergeSortSlice(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortSlice(lefthalf)
        mergeSortSlice(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)



def quickSort(aList):
    pass
