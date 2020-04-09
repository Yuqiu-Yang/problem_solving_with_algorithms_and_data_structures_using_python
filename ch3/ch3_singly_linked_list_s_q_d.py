from ch3_singly_linked_list import *


class singlyLinkedListStack:
    def __init__(self):
        self.item = UnorderedSinglyLinkedList()
    def isEmpty(self):
        return self.item.length() == 0
    def push(self, new_item):
        self.item.append(new_item)
    def pop(self):
        return self.item.pop()
    def size(self):
        return self.item.length()

class singlyLinkedListQueue:
    def __init__(self):
        self.item = UnorderedSinglyLinkedList()
    def isEmpty(self):
        return self.item.length() == 0
    def enqueue(self, item):
        self.item.add(item)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return self.item.length()

class singlyLinkedListDeque:
    def __init__(self):
        self.item = UnorderedSinglyLinkedList()
    def isEmpty(self):
        return self.item.length() == 0
    def addFront(self, item):
        self.item.append(item)
    def addRear(self, item):
        self.item.add(item)
    def removeFront(self):
        return self.item.pop()
    def removeRear(self):
        return self.item.pop(0)
    def size(self):
        return self.item.length()
