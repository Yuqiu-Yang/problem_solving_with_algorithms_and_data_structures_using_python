from ch3_singly_linked_list import *

class DoublyLinkedNode(SinglyLinkedNode):
    def __init__(self, initData):
        super().__init__(initData)
        self.back = None
    def getBack(self):
        return self.back
    def setBack(self, backNode):
        self.back = backNode


class UnorderedDoublyLinkedList(UnorderedSinglyLinkedList):
    def __init__(self):
        super().__init__()
    def add(self, item):
        """ The added item will be the first node in the list """
        self.list_size += 1
        temp = DoublyLinkedNode(item)
        temp.setNext(self.head)
        if self.list_size == 1:
            temp.setBack(self.head)
        elif self.list_size == 2:
            temp.setBack(self.head)
            self.head.setBack(temp)
        else:
            temp.setBack(self.head.getBack())
            self.head.setBack(temp)
        self.head = temp
    def append(self, item):
        self.list_size += 1
        if self.list_size == 1:
            self.list_size -= 1
            self.add(item)
        elif self.list_size == 2:
            temp = DoublyLinkedNode(item)
            self.head.setNext(temp)
            self.head.setBack(temp)
            temp.setBack(self.head)
        else:
            temp = DoublyLinkedNode(item)
            self.head.getBack().setNext(temp)
            temp.setBack(self.head.getBack())
            self.head.setBack(temp)
    def pop(self, pos = -1):
        if (pos < -1) or (pos >= (self.length())):
            raise RuntimeError("Inproper pos value")

        self.list_size -= 1
        current = self.head
        if (pos == -1) or (pos == self.length()):
            if self.length() == 0:
                temp = self.head.getData()
                self.head = None
                return temp
            else:
                self.head.getBack().getBack().setNext(None)
                temp = self.head.getBack().getData()
                if self.length() == 1:
                    self.head.setBack(None)
                else:
                    self.head.setBack(self.head.getBack().getBack())
                return temp
        else:
            count = 0
            while count != pos:
                current = current.getNext()
                count += 1
            if count == 0:
                current.getNext().setBack(self.head.getBack())
                self.head = current.getNext()
                return current.getData()
            else:
                current.getBack().setNext(current.getNext())
                current.getBack().getNext().setBack(current.getBack())
                return current.getData
    def insert(self, pos, item):
        if (pos < 0) or (pos > (self.length())):
            raise RuntimeError("Inproper pos value")
        self.list_size += 1
        if pos == 0:
            self.list_size -= 1
            self.add(item)
        elif pos == self.length() - 1:
            self.list_size -= 1
            self.append(item)
        else:
            temp = DoublyLinkedNode(item)
            current = self.head
            count = 0
            while count != pos:
                current = current.getNext()
                count += 1
            temp.setNext(current)
            temp.setBack(current.getBack())
            current.getBack().setNext(temp)
            if current.getNext() != None:
                current.getNext().setBack(temp)
