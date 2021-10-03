from node import *
from binarySearchTree import BinarySearchTree

class BinaryTree:

    def __init__(self, nodeRoot):
        self.nodeRoot = nodeRoot
        

    def insertNode(self, node, side, parent):
        if side == "R":
            if parent.hasRightChild():
                print('ERROR - o nó já tem filho direito')
            else:
                node.parent = parent
                parent.rightChild = node
        else:
            if parent.hasLeftChild():
                print('ERROR - o nó pai já tem filho esquerdo')
            else:
                node.parent = parent
                parent.leftChild =  node


    def search(self, value, NodeInicio):
        if NodeInicio == None:
            return False
        if value == NodeInicio.value:
            return True
        self.search(NodeInicio.rightChild)
        self.search(NodeInicio.lefChild)


    def nodeDegree(self, node):
        degree = 0
        if node.hasRightChild():
            degree += 1
        if node.hasLeftChild():
            degree += 1
        return degree


    def nodeDepth(self, node):
        if self.isRoot(node): 
            return 0
        else:
            parent = node.parent
            return 1 + self.nodeDepth(parent)


    def nodeHeight(self, node):
        if node.hasChild() == False or node == None:
            return 0 
        else:
            hgLeft = self.nodeHeight(node.leftChild)
            hgRight = self.nodeHeight(node.rightChild)
            return (hgLeft + 1 if hgLeft > hgRight else hgRight + 1)


    def nodeLevel(self, node):
        return self.nodeDepth(node)


    def isRoot(self, node):
            return (True if node is self.nodeRoot else False)


    def erd(self, node):

        if(node != None):
            self.erd(node.leftChild)
            print("{0}".format(node.value))
            self.erd(node.rightChild)


    def remove(self, node):
        if(node.hasBothChild()):
            print('ERROR - esta ação não é possível')
        elif(node.hasRightChild() or node.hasLeftChild()):
            rightOrLeftChild = node.rightChild if node.hasRightChild() else node.leftChild
            rightOrLeftChild.parent = node.parent

            if(node.parent.rightChild.value == node.value):
                node.parent.rightChild = rightOrLeftChild
            else:
                node.parent.leftChild = rightOrLeftChild
        else:
            if(node.parent.rightChild.value == node.value):
                node.parent.rightChild = None
            else:
                node.parent.leftChild = None


    def __navigationLRN(self, node):
        if node == None:
            return None

        self.__navigationLRN(node.leftChild)
        self.__navigationLRN(node.rightChild)
        print(node.value)


    def __navigationLNR(self, node):
        if node == None:
            return None

        self.__navigationLNR(node.leftChild)
        print(node.value)
        self.__navigationLNR(node.rightChild)
    

    def __navigationNLR(self, node):
        if node == None:
            return None

        print(node.value)
        self.__navigationNLR(node.leftChild)
        self.__navigationNLR(node.rightChild)


    def navigation(self, typeOfNavigation, node):
        return {
            'LRN': self.__navigationLRN,
            'LNR': self.__navigationLNR,
            'NLR': self.__navigationNLR
        }[typeOfNavigation](node)


    def getAllNodes(self, currentNode, nodes=[]):
        if currentNode == None:
            return None
        
        nodes.append(Node(currentNode.value))

        self.getAllNodes(currentNode.leftChild, nodes)
        self.getAllNodes(currentNode.rightChild, nodes)

        return nodes


    def transformBinaryTreeIntoBinarySearchTree(self, node=None):
        if node == None:
            node = self.nodeRoot

        nodes = self.getAllNodes(node)
        
        binarySearch = BinarySearchTree()

        for _node in nodes:
            binarySearch.insertNode(_node)


    
    def toString(self, node):
        result = '  '
        if(node != None):
            if self.isRoot(node):
                print(node.value)
            if(node.hasLeftChild() == True):
                result += node.leftChild.value + ' '
                self.toString(node.leftChild)
            elif(node.hasRightChild() == True):
                result += node.rightChild.value + ''
                self.toString(node.rightChild) 
            print(result)
               
