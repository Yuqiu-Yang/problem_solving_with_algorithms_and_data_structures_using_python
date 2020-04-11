def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    print("Moving disk from %d to %d\n" % (fromPole, toPole))

moveTower(10, 1,3,2)
