class TreeNode:
    def __init__(self, key, val, left = None, right = None,\
                parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0
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
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    def findNextLargest(self):
        if self.rightChild:
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findNextLargest()
                    self.parent.rightChild = self
        return succ
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent
        def __iter__(self):
            if self:
                if self.hasLeftChild():
                    for elem in self.leftChild:
                        yield elem
                yield self.key
                if self.hasRightChild():
                    for elem in self.rightChild:
                        yield elem
class BinarySearchTree:
    def __init__(self):
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
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None
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
            return currentNode
    def __getitem__(self, key):
        return self.get(key)
    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False
    def delete(self, key):
        if self.size == 0:
            raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in Tree')
    def __delitem__(self, key):
        self.delete(key)
    def remove(self, node):
        if node.isLeaf():
            # Note in this case, we do not need to consider
            # the situation where the node is the root
            # since it's been handelled by the second if
            # clause in the delete function
            if node.isLeftChild():
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        elif node.hasBothChildren():
            succ = node.findNextLargest()
            succ.spliceOut()
            node.key = succ.key
            node.payload = succ.payload
        else:
            # If the node only has one child
            if node.hasLeftChild():
                # if the the child is left child
                if node.isLeftChild():
                    node.parent.leftChild = node.leftChild
                    node.leftChild.parent = node.parent
                elif node.isRightChild():
                    node.parent.rightChild = node.leftChild
                    node.leftChild.parent = node.parent
                else:
                    node.replaceNodeData(node.leftChild.key,
                                         node.leftChild.payload,
                                         node.leftChild.leftChild,
                                         node.leftChild.rightChild)
            else:
                # if the child is right child
                if node.isLeftChild():
                    node.parent.leftChild = node.rightChild
                    node.rightChild.parent = node.parent
                elif node.isRightChild():
                    node.parent.rightChild = node.rightChild
                    node.rightChild.parent = node.parent
                else:
                    node.replaceNodeData(node.rightChild.key,
                                         node.rightChild.payload,
                                         node.rightChild.leftChild,
                                         node.rightChild.rightChild)



def BinarySearchTreeInorderTraversal(bTree):
    root = bTree.root
    minNode = root.findMin()
    print(minNode.key)
    succNode = minNode.findNextLargest()
    if succNode:
        print(succNode.key)
    else:
        while True:
            succNode = succNode.findNextLargest()
            if succNode:
                print(succNode.key)
            else:
                break
    print(root.key)
    if root.hasRightChild():
        minNode = root.rightChild.findMin()
        print(minNode.key)
        succNode = minNode.findNextLargest()
        if succNode:
            print(succNode.key)
        else:
            while True:
                succNode = succNode.findNextLargest()
                if succNode:
                    print(succNode.key)
                else:
                    break
