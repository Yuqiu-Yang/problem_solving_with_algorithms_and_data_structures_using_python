from ch3_queue import Queue
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
    def __init__(self, time):
        self.timeStamp = time
        self.pages = random.randint(1,20)
    def getPages(self):
        return self.pages
    def getStamp(self):
        return self.timeStamp
    def waitTime(self, currentTime):
        return currentTime - self.timeStamp

def newPrintTask():
    num = random.randrange(1, 181)
    return num == 180

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(\
            nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)
        labprinter.tick()

    averageWait = sum(waitingTimes)/len(waitingTimes)
    print("Average wait %6.2f secs %3d tasks remaining"\
    %(averageWait, printQueue.size()))
