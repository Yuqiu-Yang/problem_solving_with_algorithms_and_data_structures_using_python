def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    print("Moving disk from %d to %d\n" % (fromPole, toPole))

moveTower(1, 1,3,2)


from ch3_stack import *
def moveTowerStack(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTowerStack(height - 1, fromPole, withPole, toPole)
        moveDiskStack(fromPole, toPole)
        moveTowerStack(height - 1, withPole, toPole, fromPole)

def moveDiskStack(fromPole, toPole):
    temp = fromPole.pop()
    toPole.push(temp)


height = 3
fromPole = Stack()
for i in range(height):
    fromPole.push(i + 1)
toPole = Stack()
withPole = Stack()
moveTowerStack(height, fromPole, toPole, withPole)

for i in range(height):
    print(toPole.pop())
