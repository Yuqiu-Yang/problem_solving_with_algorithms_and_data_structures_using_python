class SinglyLinkedNode:
    def __init__(self, initData):
        self.data = initData
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, nextNode):
        self.next = nextNode


class UnorderedSinglyLinkedList:
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
    def add(self,item):
        """ The added item will be the first node in the list """
        self.list_size += 1
        temp = SinglyLinkedNode(item)
        temp.setNext(self.head)
        self.head = temp
    def length_traverse(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def remove(self, item):
        pass

    def remove_all(self, item):
        pass

    def search(self, item):
        """ Check if item is present in the list"""
        current = self.head
        found = False
        while (not found) and (current != None):
            temp = current.getData()
            if temp == item:
                found = True
            else:
                current = current.getNext()
        return found

    def append(self, item):
        pass
    def index(self, item):
        current = self.head
        ind = None
        count = 0
        while (ind == None) and (current != None):
            temp = current.getData()
            if temp == item:
                ind = count
            else:
                current = current.getNext()
                count += 1
        return ind

    def index_all(self, item):
        pass

    def insert(self, pos, item):
        pass
    def pop(self, pos = -1):
        pass


    def slice(self, start, stop):
        pass
