class Queue(object):
    def __init__(self):
        self.item = []
        self.queue_size = 0
    def isEmpty(self):
        return self.queue_size == 0
    def enqueue(self, item):
        self.item.insert(0, item)
        self.queue_size += 1
    def dequeue(self):
        self.queue_size -= 1
        return self.item.pop()
    def size(self):
        return self.queue_size


class revQueue(object):
    def __init__(self):
        self.item = []
        self.queue_size = 0
    def isEmpyt(self):
        return self.queue_size == 0
    def enqueue(self, item):
        self.queue_size += 1
        self.item.append(item)
    def dequeue(self):
        self.queue_size -= 1
        return self.item.pop(0)
    def size(self):
        return self.queue_size

class O1Queue(object):
    def __init__(self):
        self.item = []
        self.start_ind = 0
        self.queue_size = 0
    def enqueue(self, item):
        self.queue_size += 1
        self.item.append(item)
    def dequeue(self):
        self.queue_size -= 1
        temp = self.item[self.start_ind]
        self.start_ind += 1
        return temp
    def isEmpty(self):
        return self.queue_size == 0
    def size(self):
        return self.queue_size


from ch3_doubly_linked_list import *

class doublyLinkedListQueue:
    def __init__(self):
        self.item = UnorderedDoublyLinkedList()
    def enqueue(self, item):
        self.item.add(item)
    def dequeue(self):
        return self.item.pop()
    def isEmpty(self):
        return self.item.length() == 0
    def size(self):
        return self.item.length()
