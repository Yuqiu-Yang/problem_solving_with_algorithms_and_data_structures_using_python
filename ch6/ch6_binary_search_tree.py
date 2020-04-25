class TreeNode:
    def __init__(self, key, val, left = None, right = None,\
                parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    def isLeftChild(self):
        return (self.parent) and (self.parent.leftChild == self)
    def isRightChild(self):
        return (self.parent) and (self.parent.rightChild == self)
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.leftChild or self.rightChild)
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild
    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:
    def __inif__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)
        else:
            currentNode.replaceNodeData(key, val, currentNode.leftChild, currentNode.rightChild)
    def __setitem__(self, key, val):
        self.put(key, val)

    def get(self, key):
        if self.root:
            return self._get(key, self.root)
        else:
            return None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            return self._get(key, currentNode.rightChild)
        else:
            return currentNode.payload
    def __getitem__(key):
        return self.get(key)
            
