from node import *

class BinarySearchTree:

    def __init__(self):
        self.nodeRoot = None

    
    def insertNode(self, node, root=None):
        if self.nodeRoot == None:
            self.nodeRoot = node
            return

        if root == None:
            root = self.nodeRoot

        if node.value < root.value and not root.hasLeftChild():
            root.leftChild = node
            return
        
        if node.value >= root.value and not root.hasRightChild():
            root.rightChild = node
            return

        return self.insertNode(node, root.leftChild) if node.value < root.value else self.insertNode(node, root.rightChild)


    def navigation(self, node):
        if node == None:
            return None

        self.navigation(node.leftChild)
        print(node.value)
        self.navigation(node.rightChild)

