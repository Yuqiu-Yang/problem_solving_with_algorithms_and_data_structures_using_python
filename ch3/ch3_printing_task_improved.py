from ch3_queue import Queue()

import random

class Printer:
    def __init__(self, ppm):
        self.pageRate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def busy(self):
        return self.currentTask != None
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() \
        *60/self.pageRate


class Task:
    pass

class Computer:
    pass
