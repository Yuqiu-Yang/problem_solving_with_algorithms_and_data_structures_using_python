from random import randrange

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
