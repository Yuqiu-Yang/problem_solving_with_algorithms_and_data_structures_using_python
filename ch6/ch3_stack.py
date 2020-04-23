class Stack(object):
    def __init__(self):
        self.items = []
        self.stack_size = 0
    def isEmpty(self):
        return self.stack_size == 0
    def push(self, new_item):
        self.items.append(new_item)
        self.stack_size += 1
    def pop(self):
        self.stack_size -= 1
        return self.items.pop()
    def peek(self):
        return self.items[self.stack_size - 1]
    def size(self):
        return self.stack_size
