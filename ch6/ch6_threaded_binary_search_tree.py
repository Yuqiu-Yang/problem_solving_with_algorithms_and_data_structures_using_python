from ch6_binary_search_tree import *

class threadedTreeNode(TreeNode):
    def __init__(self, key, val, left = None, right = None,\
                parent = None,successor = None):
        super().__init__(key, val, left, right, parent)
        self.successor = successor

class threadedBinarySearchTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = threadedTreeNode(key, val)
        self.size += 1

        current = self.root.findMin()
        while not current.isRoot():
            succ = current.findNextLargest()
            current.successor = succ
            current = succ
        # Now current should point to the root
        # Its successor should be the smallest node
        # in the right subtree
        if current.hasRightChild():
            current.successor = current.rightChild.findMin()
            current = current.successor
            while current:
                succ = current.findNextLargest()
                current.successor = succ
                current = succ

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = threadedTreeNode(key, val, parent = currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = threadedTreeNode(key, val, parent = currentNode)
        else:
            currentNode.replaceNodeData(key, val, currentNode.leftChild, currentNode.rightChild,\
                                        currentNode.successor)
    def __setitem__(self, key, val):
        self.put(key, val)


def threadedTreeInorderTraversal(threadedBTree):
    current = threadedBTree.root.findMin()
    while current.successor != None:
        print(current.key)
        current = current.successor
    print(current.key)
