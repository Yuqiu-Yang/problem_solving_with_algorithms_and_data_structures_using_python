from ch3_queue import Queue

import random

def hotPotato(nameList, minNum, maxNum):
    simQueue = Queue()
    for name in nameList:
        simQueue.enqueue(name)
    while simQueue.size() > 1:
        num = random.randint(minNum, maxNum)
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())
        simQueue.dequeue()
    return simQueue.dequeue()
