def sequentialSearch(aList, item):
    pos = 0
    found = False
    while pos < len(aList) and (not found):
        if aList[pos] == item:
            found = True
        else:
            pos += 1
    return found

def orderedSequentialSearch(aList, item, order = 'ascending'):
    pos = 0
    found = False
    stop = False
    while (pos < len(aList)) and (not found) and (not stop):
        if aList[pos] == item:
            found = True
        else:
            if order == "ascending":
                if aList[pos] > item:
                    stop = True
            else:
                if aList[pos] < item:
                    stop = True
            pos += 1
    return found


def binarySearch(aList, item, order = "ascending"):
    first = 0
    last = len(aList) - 1
    found = False
    while (first <= last) and (not found):
        midPoint = (first + last)//2
        if aList[midPoint] == item:
            found = True
        else:
            if order == "ascending":
                if aList[midPoint] > item:
                    last = midPoint - 1
                else:
                    first = midPoint + 1
            else:
                if aList[midPoint] < item:
                    last = midPoint - 1
                else:
                    first = midPoint + 1
    return found



def binarySearchRecursive(aList, item, order = "ascending"):
    if len(aList) == 0:
        return False
    else:
        midPoint = len(aList)//2
        if aList[midPoint] == item:
            return True
        else:
            if order == "ascending":
                if aList[midPoint] > item:
                    return binarySearchRecursive(aList[:midPoint], item, order = "ascending")
                else:
                    return binarySearchRecursive(aList[(midPoint + 1):], item, order = "ascending")
            else:
                if aList[midPoint] < item:
                    return binarySearchRecursive(aList[:midPoint], item, order = "descending")
                else:
                    return binarySearchRecursive(aList[(midPoint + 1):], item, order = "descending")



def binarySearchRecursive1(aList, item, first, last, order = "ascending"):
    if (last < first):
        return False 
    else:
        midPoint = (first + last)//2
        if aList[midPoint] == item:
            return True
        else:
            if order == "ascending":
                if aList[midPoint] > item:
                    return binarySearchRecursive1(aList, item, first, midPoint - 1, order = "ascending")
                else:
                    return binarySearchRecursive1(aList, item, midPoint + 1, last, order = "ascending")
            else:
                if aList[midPoint] < item:
                    return binarySearchRecursive1(aList, item, first, midPoint - 1, order = "descending")
                else:
                    return binarySearchRecursive1(aList, item, midPoint + 1, last, order = "descending")
