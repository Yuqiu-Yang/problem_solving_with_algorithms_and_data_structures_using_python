def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 0:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2, [newBranch, t, []])
    else:
        root.insert(2, [newBranch, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
print(r)
insertLeft(r, 4)
print(r)
insertLeft(r, 5)
print(r)
