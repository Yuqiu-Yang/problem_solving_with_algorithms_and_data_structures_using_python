class Queue(object):
    def __init__(self):
        self.item = []
        self.queue_size = 0
    def isEmpty(self):
        return self.queue_size == 0
    
