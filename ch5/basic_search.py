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
