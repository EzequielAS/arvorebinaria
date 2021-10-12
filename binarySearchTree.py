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


    def printTree(self, node, counter=0):
        if node == None:
            return None

        newCounter = counter
        blankSpace = ' '*counter
        
        print(f'{blankSpace}{node.value}')
        self.printTree(node.rightChild if node.rightChild != None else None, newCounter+1)
        self.printTree(node.leftChild if node.leftChild != None else None, newCounter+1)

