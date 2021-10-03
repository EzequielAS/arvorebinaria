from node import *

class BinarySearchTree:

    def __init__(self, nodeRoot):
        self.nodeRoot = nodeRoot

    
    def insertNode(self, node, root=None):
        if root == None:
            root = self.nodeRoot

        if node.value < root.value and not root.hasLeftChild():
            root.leftChild = node
            return
        
        if node.value > root.value and not root.hasRightChild():
            root.rightChild = node
            return

        return self.insertNode(node, root.leftChild) if node.value < root.value else self.insertNode(node, root.rightChild)


    def navigation(self, node):
        if node == None:
            return None

        self.navigation(node.leftChild)
        print(node.value)
        self.navigation(node.rightChild)




nodeRoot = Node(6)
binarySearch = BinarySearchTree(nodeRoot)

nodeB = Node(2)
nodeC = Node(5)
nodeD = Node(8)
nodeE = Node(1)
nodeF = Node(29)

binarySearch.insertNode(nodeB)
binarySearch.insertNode(nodeC)
binarySearch.insertNode(nodeD)
binarySearch.insertNode(nodeE)
binarySearch.insertNode(nodeF)

binarySearch.navigation(nodeRoot)