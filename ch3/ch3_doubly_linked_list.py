from ch3_singly_linked_list import *

class DoublyLinkedNode(SinglyLinkedNode):
    def __init__(self, initData):
        super().__init__(initData)
        self.back = None
    def getBack(self):
        return self.back
    def setBack(self, backNode):
        self.back = backNode


class UnorderedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.list_size = 0
    def __str__(self):
        listString = "["
        current = self.head
        while current != None:
            if current.getNext() != None:
                listString += (str(current.getData()) + ", ")
            else:
                listString += str(current.getData())
            current = current.getNext()

        return listString + "]"
    def isEmpty(self):
        return self.head == None
    def length(self):
        return self.list_size
