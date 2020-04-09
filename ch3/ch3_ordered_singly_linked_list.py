from ch3_singly_linked_list import *

class OrderedSinglyLinkedList(UnorderedSinglyLinkedList):
    def __init__(self, ascending = True):
        super().__init__()
        self.ascending = ascending
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while (not found) and (current != None) and (not Stop):
            temp = current.getData()
            if temp == item:
                found = True
            else:
                if self.ascending:
                    if temp > item:
                        stop = True
                    else:
                        current = current.getNext()
                else:
                    if temp < item:
                        stop = True
                    else:
                        current = current.getNext()
        return found
    def add(self, item):
        self.list_size += 1
        temp = SinglyLinkedNode(item)
        current = self.head
        previous = None

        if self.ascending:
            while (current!=None) and (current.getData() <= item):
                previous = current
                current = current.getNext()
        else:
            while (current!=None) and (current.getData() >= item):
                previous = current
                current = current.getNext()
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    def append(self, item):
        raise AttributeError("OrderedSinglyLinkedList object has no attribute 'append'")

    def insert(self, pos, item):
        raise AttributeError("OrderedSinglyLinkedList object has no attribute 'insert'")
