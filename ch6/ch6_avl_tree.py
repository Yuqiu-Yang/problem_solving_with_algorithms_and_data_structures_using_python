from ch6_binary_search_tree import *



class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)
                self.updateBalance(currentNode.rightChild)
    def updateBalance(self, node, mode = 'put'):
        if mode == 'put':
            if node.balanceFactor > 1 or node.balanceFactor < -1:
                self.rebalance(node)
                return
            # if we want to put node
            if node.parent != None:
                if node.isLeftChild():
                    node.parent.balanceFactor += 1
                else:
                    node.parent.balanceFactor -= 1
                if node.parent.balanceFactor != 0:
                    self.updateBalance(node.parent)
        else:
            if node.balanceFactor > 1 or node.balanceFactor < -1:
                self.rebalance(node)
            # if we want to delete node
            # Since it's an AVL tree
            # the balance factor of any node can only
            # take on values 0, -1, 1
            if node.parent != None:
                # If node has two children
                # then we will find the next-largest
                # which has at most one child
                # and we will update the balance factors
                # from there
                if node.parent.balanceFactor == 0:
                    # if the subtree is balanced
                    # deleting a node won't affect
                    # the height of the subtree rooted at node.parent
                    if node.isLeftChild():
                        print("balance subtract 1")
                        node.parent.balanceFactor -= 1
                    else:
                        print("balance add 1")
                        node.parent.balanceFactor += 1
                elif node.parent.balanceFactor == 1:
                    # if the subtree is left heavy
                    if node.isLeftChild():
                        # if the node is the left child
                        # then after deletion the subtree
                        # rooted at node.parent will be balanced
                        # since the height of the subtree changed
                        # we need to update the balance factors
                        # of the grand parents
                        print("left subtract 1")
                        node.parent.balanceFactor -= 1
                        self.updateBalance(node.parent, mode = "delete")
                    else:
                        # if the node is the right child
                        # then deleting it won't affect the
                        # height of the subtree
                        # But we need to consider rotation
                        print("left add 1")
                        node.parent.balanceFactor += 1
                        if node.parent.balanceFactor > 1:
                            self.updateBalance(node.parent, mode = "delete")
                elif node.parent.balanceFactor == -1:
                    # if the subtree is right heavy
                     if node.isLeftChild():
                         print("right subtract 1")
                         node.parent.balanceFactor -= 1
                         if node.parent.balanceFactor < -1:
                             self.updateBalance(node.parent, mode = "delete")
                     else:
                         print("right subtract 1")
                         node.parent.balanceFactor += 1
                         self.updateBalance(node.parent, mode = "delete")

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1\
                                - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1\
                                + max(rotRoot.balanceFactor, 0)
    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor += -1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor += -1 + min(rotRoot.balanceFactor, 0)
    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)
    def remove(self, node):
        if node.isLeaf():
            # Note in this case, we do not need to consider
            # the situation where the node is the root
            # since it's been handelled by the second if
            # clause in the delete function
            self.updateBalance(node, mode = "delete")
            if node.isLeftChild():
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
        elif node.hasBothChildren():
            # since has both children
            # the next laregest will always
            # be the left most node in the subtree
            succ = node.findNextLargest()
            temp = succ.parent
            self.updateBalance(succ, mode = "delete")
            succ.spliceOut()
            node.key = succ.key
            node.payload = succ.payload
        else:
            # If the node only has one child
            if node.hasLeftChild():
                # if the the child is left child
                if node.isLeftChild():
                    self.updateBalance(node, mode = "delete")
                    node.parent.leftChild = node.leftChild
                    node.leftChild.parent = node.parent
                elif node.isRightChild():
                    self.updateBalance(node, mode = "delete")
                    node.parent.rightChild = node.leftChild
                    node.leftChild.parent = node.parent
                else:
                    node.replaceNodeData(node.leftChild.key,
                                         node.leftChild.payload,
                                         node.leftChild.leftChild,
                                         node.leftChild.rightChild,
                                         node.leftChild.balanceFactor)
            else:
                # if the child is right child
                if node.isLeftChild():
                    self.updateBalance(node, mode = "delete")
                    node.parent.leftChild = node.rightChild
                    node.rightChild.parent = node.parent
                elif node.isRightChild():
                    self.updateBalance(node, mode = "delete")
                    node.parent.rightChild = node.rightChild
                    node.rightChild.parent = node.parent
                else:
                    node.replaceNodeData(node.rightChild.key,
                                         node.rightChild.payload,
                                         node.rightChild.leftChild,
                                         node.rightChild.rightChild,
                                         node.rightChild.balanceFactor)
