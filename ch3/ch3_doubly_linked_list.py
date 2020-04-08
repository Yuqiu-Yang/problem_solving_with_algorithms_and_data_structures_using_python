class DoublyLinkedNode:
    def __init__(self, initData):
        self.data = initData
        self.next = None
        self.back = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getBack(self):
        return self.back
    def setData(self, newData):
        self.data = newData
    def setNext(self, nextNode):
        self.next = nextNode
    def setBack(self, backNode):
        self.back = backNode
