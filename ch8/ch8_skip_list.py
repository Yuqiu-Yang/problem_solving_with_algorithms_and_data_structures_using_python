from random import randrange
from ch3_stack import *
def flip():
    return randrange(2)


class HeaderNode:
    def __init__(self):
        self.next = None
        self.down = None
    def getNext(self):
        return self.next
    def getDown(self):
        return self.down
    def setNext(self, newnext):
        self.next = newnext
    def setDown(self, newdown):
        self.down = newdown


class DataNode:
    def __init__(self, key, value):
        self.key = key
        self.data = value
        self.next = None
        self.down = None
    def getKey(self):
        return self.key
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getDown(self):
        return self.down
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
    def setDown(self, newdown):
        self.down = newdown


class SkipList:
    def __init__(self):
        self.head = None

    def search(self, key):
        current = self.head
        found = False
        stop = False
        while not found and not stop:
            if current == None:
                stop = True
            else:
                if current.getNext() == None:
                    current = current.getDown()
                else:
                    if current.getNext().getKey() == key:
                        found = True
                    else:
                        if key < current.getNext().getKey():
                            current = current.getDown()
                        else:
                            current = current.getNext()
        if found:
            return current.getNext().getData()
        else:
            return None
    def insert(self, key, data):
        if self.head == None:
            self.head = HeaderNode()
            temp = DataNode(key, data)
            self.head.setNext(temp)
            top = temp
            while flip() == 1:
                newhead = HeaderNode()
                temp = DataNode(key, data)
                temp.setDown(top)
                newhead.setNext(temp)
                newhead.setDown(self.head)
                self.head = newhead
                top = temp
        else:
            towerStack = Stack()
            current = self.head
            stop = False
            while not stop:
                if current == None:
                    stop = True
                else:
                    if current.getNext() == None:
                        towerStack.push(current)
                        current = current.getDown()
                    else:
                        if current.getNext().getKey() > key:
                            towerStack.push(current)
                            current = current.getDown()
                        else:
                            current = current.getNext()
            lowestLevel = towerStack.pop()
            temp = DataNode(key, data)
            temp.setNext(lowestLevel.getNext())
            lowestLevel.setNext(temp)
            top = temp
            while flip() == 1:
                if towerStack.isEmpty():
                    newhead = HeaderNode()
                    temp = DataNode(key, data)
                    temp.setDown(top)
                    newhead.setDown(self.head)
                    newhead.setNext(temp)
                    self.head = newhead
                    top = temp
                else:
                    nextLevel = towerStack.pop()
                    temp = DataNode(key, data)
                    temp.setDown(top)
                    temp.setNext(nextLevel.getNext())
                    nextLevel.setNext(temp)
                    top = temp
    def __delitem__(self, key):
        current = self.head
        found = False
        stop = False
        towerStack = Stack()
        while not found and not stop:
            if current == None:
                stop = True
            else:
                if current.getNext() == None:
                    current = current.getDown()
                else:
                    if current.getNext().getKey() == key:
                        found = True
                    else:
                        if key < current.getNext().getKey():
                            current = current.getDown()
                        else:
                            current = current.getNext()

        if found:
            stop = False
            while not stop:
                if current == None:
                    stop = True
                else:
                    if current.getNext().getKey() == key:
                        towerStack.push(current)
                        current = current.getDown()
                    else:
                        current = current.getNext()
            while not towerStack.isEmpty():
                nodeBefore = towerStack.pop()
                nodeBefore.getNext().setDown(None)
                temp = nodeBefore.getNext().getNext()
                nodeBefore.setNext(temp)
        else:
            raise KeyError('Key is not in the list')

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, data):
        self.insert(key, data)
    def __contains__(self, key):
        if self.search(key):
            return True
        else:
            return False
    def keys(self):
        current = self.head
        stop = False
        while not stop:
            if current.getDown() == None:
                stop = True
            else:
                current = current.getDown()
        keyList = []

        stop = False
        while not stop:
            if current.getNext() == None:
                stop = True
            else:
                current = current.getNext()
                keyList.append(current.getKey())
        return keyList
    def values(self):
        current = self.head
        stop = False
        while not stop:
            if current.getDown() == None:
                stop = True
            else:
                current = current.getDown()
        valueList = []

        stop = False
        while not stop:
            if current.getNext() == None:
                stop = True
            else:
                current = current.getNext()
                valueList.append(current.getData())
        return valueList
    def printWholeList(self):
        keyList = self.keys()
        listRep = []
        towerStack = Stack()
        current = self.head
        stop = False
        while not stop:
            towerStack.push(current)
            if current.getDown() == None:
                stop = True
            else:
                current = current.getDown()
        while not towerStack.isEmpty():
            currentHead = towerStack.pop()
            temp = []
            stop = False
            current = currentHead.getNext()
            for c in range(len(keyList)):
                if current == None:
                    temp.append((None, None)) 
                else:
                    if current.getKey() != keyList[c]:
                        temp.append((None, None))
                    else:
                        temp.append((current.getKey(), current.getData()))
                        current = current.getNext()


            listRep.append(temp)
        return listRep[::-1]
class Map:
    def __init__(self):
        self.collection = SkipList()
    def put(self, key, data):
        self.collection.insert(key, data)
    def get(self, key):
        return self.collection.search(key)
    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, data):
        self.put(key, data)
    def keys(self):
        return self.collection.keys()
    def values(self):
        return self.collection.values()
    def __contains__(self, key):
        return key in self.collection
    def __delitem__(self, key):
        del self.collection[key]
