class Deque:
    def __init__(self):
        self.item = []
        self.deque_size = 0
    def isEmpty(self):
        return self.deque_size == 0
    def addFront(self, item):
        self.deque_size += 1
        self.item.append(item)
    def addRear(self, item):
        self.deque_size += 1
        self.item.insert(0, item)
    def removeFront(self):
        self.deque_size -= 1
        return self.item.pop()
    def removeRear(self):
        self.deque_size -= 1
        return self.item.pop(0)
    def size(self):
        return self.deque_size
